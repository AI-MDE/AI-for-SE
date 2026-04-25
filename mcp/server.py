from __future__ import annotations

import json
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("ai-mde")


def workspace_root() -> Path:
    return Path(os.environ.get("MDE_WORKSPACE", ".")).resolve()


def mde_dir() -> Path:
    return workspace_root() / ".mde"


def skills_dir() -> Path:
    return workspace_root() / ".ai" / "skills"


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def write_text(path: Path, content: str) -> None:
    ensure_dir(path.parent)
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: Dict[str, Any]) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_command(args: List[str], cwd: Optional[Path] = None) -> Dict[str, Any]:
    root = cwd or workspace_root()
    try:
        result = subprocess.run(
            args,
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        return {
            "command": args,
            "cwd": str(root),
            "returncode": result.returncode,
            "stdout": result.stdout[-4000:],
            "stderr": result.stderr[-4000:],
            "ok": result.returncode == 0,
        }
    except FileNotFoundError as exc:
        return {
            "command": args,
            "cwd": str(root),
            "returncode": 127,
            "stdout": "",
            "stderr": str(exc),
            "ok": False,
        }


def slugify(value: str) -> str:
    cleaned = "".join(ch.lower() if ch.isalnum() else "-" for ch in value)
    while "--" in cleaned:
        cleaned = cleaned.replace("--", "-")
    return cleaned.strip("-") or "work-item"


def mde_path(*parts: str) -> Path:
    return mde_dir().joinpath(*parts)


@mcp.tool()
def mde_scan_codebase() -> Dict[str, Any]:
    """Scan codebase and generate baseline project configuration and code-map artifacts."""
    root = workspace_root()
    base = mde_dir()
    ensure_dir(base / "models")
    ensure_dir(base / "reports")

    package_json = root / "package.json"
    tsconfig = root / "tsconfig.json"

    stack: List[str] = []
    scripts: Dict[str, Any] = {}
    dependencies: Dict[str, Any] = {}

    if package_json.exists():
        try:
            pkg = json.loads(package_json.read_text(encoding="utf-8"))
            scripts = pkg.get("scripts", {})
            dependencies = {
                "dependencies": pkg.get("dependencies", {}),
                "devDependencies": pkg.get("devDependencies", {}),
            }
            stack.append("node")
            if "typescript" in dependencies.get("devDependencies", {}) or tsconfig.exists():
                stack.append("typescript")
        except Exception as exc:
            scripts = {"error": str(exc)}

    source_dirs = [str(p.relative_to(root)) for p in root.iterdir() if p.is_dir() and not p.name.startswith(".")]

    project_config = {
        "generatedAt": now_iso(),
        "workspace": str(root),
        "stack": stack,
        "sourceDirs": source_dirs,
        "hasPackageJson": package_json.exists(),
        "hasTsConfig": tsconfig.exists(),
        "scripts": scripts,
        "dependencies": dependencies,
        "skillsDir": str(skills_dir().relative_to(root)) if skills_dir().exists() else ".ai/skills",
    }

    write_json(base / "models" / "project-configuration.json", project_config)

    analyze_result = run_command(["npm", "run", "analyze"], cwd=root) if package_json.exists() else {
        "ok": False,
        "stdout": "",
        "stderr": "package.json not found; skipped npm run analyze",
    }

    legacy_code_map = root / ".ai" / "code-map.full.json"
    target_code_map = base / "models" / "codebase-model.json"
    if legacy_code_map.exists():
        ensure_dir(target_code_map.parent)
        target_code_map.write_text(legacy_code_map.read_text(encoding="utf-8"), encoding="utf-8")

    report = f"""# Codebase Scan Summary

Generated: {now_iso()}

## Outputs

- `.mde/models/project-configuration.json`
- `.mde/models/codebase-model.json` if analyzer succeeded

## Analyzer Result

```text
ok: {analyze_result.get('ok')}
returncode: {analyze_result.get('returncode')}
```

## Notes

This command is artifact-first. Full artifacts are written locally; only this summary is returned to the AI.

Skills, if present, live under `.ai/skills/`.
"""
    write_text(base / "reports" / "codebase-scan-summary.md", report)

    return {
        "status": "completed",
        "workspace": str(root),
        "outputs": [
            ".mde/models/project-configuration.json",
            ".mde/reports/codebase-scan-summary.md",
            ".mde/models/codebase-model.json",
        ],
        "analyzeOk": analyze_result.get("ok"),
        "message": "Codebase scan completed. MDE artifacts were written to .mde/. Skills remain under .ai/skills/.",
    }


@mcp.tool()
def mde_understand_data_model(source: str = "auto", path: str = "") -> Dict[str, Any]:
    """Inspect database/schema artifacts and create a draft data model."""
    root = workspace_root()
    base = mde_dir()
    ensure_dir(base / "models")
    ensure_dir(base / "evidence")
    ensure_dir(base / "reports")

    candidates: List[str] = []
    search_roots = [root / path] if path else [root]
    extensions = {".sql", ".prisma"}
    names = {"schema.prisma", "ormconfig.json", "data-source.ts"}

    for search_root in search_roots:
        if not search_root.exists():
            continue
        for item in search_root.rglob("*"):
            if ".git" in item.parts or "node_modules" in item.parts:
                continue
            if item.is_file() and (item.suffix in extensions or item.name in names):
                candidates.append(str(item.relative_to(root)))

    evidence = {
        "generatedAt": now_iso(),
        "source": source,
        "path": path,
        "candidateFiles": candidates,
    }
    write_json(base / "evidence" / "data-model-sources.json", evidence)

    draft = f"""# Data Model Draft

Generated: {now_iso()}

## Source

- source: `{source}`
- path: `{path or '.'}`

## Candidate Schema Artifacts

{chr(10).join(f'- `{c}`' for c in candidates) if candidates else '- No schema artifacts found.'}

## AI Interpretation Required

The next AI step should inspect the candidate artifacts and infer:

- logical entities
- attributes
- relationships
- lifecycle/status fields
- database constraints
- views/triggers/audit behavior
- gaps between code model and database model

"""
    write_text(base / "models" / "data-model.draft.md", draft)
    write_text(base / "reports" / "data-model-understanding-report.md", draft)

    return {
        "status": "completed",
        "candidateFileCount": len(candidates),
        "outputs": [
            ".mde/evidence/data-model-sources.json",
            ".mde/models/data-model.draft.md",
            ".mde/reports/data-model-understanding-report.md",
        ],
        "message": "Data model evidence collected. AI interpretation should review the generated draft and candidate files.",
    }


@mcp.tool()
def mde_capture_requirements_from_codebase(module: str = "") -> Dict[str, Any]:
    """Create a draft requirements model from codebase evidence."""
    root = workspace_root()
    base = mde_dir()
    ensure_dir(base / "models")
    ensure_dir(base / "reports")

    code_map = base / "models" / "codebase-model.json"
    draft = f"""# Requirements Draft

Generated: {now_iso()}

## Scope

- module: `{module or 'all'}`

## Evidence

- codebase model exists: `{code_map.exists()}`

## AI Interpretation Required

Infer visible features, user actions, business rules, and gaps from controllers, handlers, domain objects, tests, and documentation.

"""
    write_text(base / "models" / "requirements.draft.md", draft)
    write_text(base / "reports" / "requirements-capture-report.md", draft)

    return {
        "status": "completed",
        "outputs": [
            ".mde/models/requirements.draft.md",
            ".mde/reports/requirements-capture-report.md",
        ],
        "message": "Requirements draft artifact created. AI should now fill it from selected evidence.",
    }


@mcp.tool()
def mde_capture_architecture_from_codebase(area: str = "") -> Dict[str, Any]:
    """Create a draft architecture and patterns model from codebase evidence."""
    root = workspace_root()
    base = mde_dir()
    ensure_dir(base / "models")
    ensure_dir(base / "reports")

    draft = f"""# Architecture and Patterns Draft

Generated: {now_iso()}

## Scope

- area: `{area or 'all'}`

## Skills Directory

- `.ai/skills/`

## AI Interpretation Required

Extract only observed patterns:

- folder/layer structure
- dependency direction
- command/query patterns
- validation approach
- repository usage
- error handling
- transaction handling
- test structure

For each pattern, include examples, inconsistencies, and canonical recommendation.

"""
    write_text(base / "models" / "architecture-and-patterns.draft.md", draft)
    write_text(base / "reports" / "architecture-capture-report.md", draft)

    return {
        "status": "completed",
        "outputs": [
            ".mde/models/architecture-and-patterns.draft.md",
            ".mde/reports/architecture-capture-report.md",
        ],
        "message": "Architecture draft artifact created. AI should now fill it from selected evidence.",
    }


@mcp.tool()
def mde_generate_work_items_from_git_issues(repo: str, label: str = "") -> Dict[str, Any]:
    """Create placeholder work-item import report for GitHub issues."""
    base = mde_dir()
    ensure_dir(base / "work-items")
    ensure_dir(base / "reports")

    report = f"""# GitHub Issues Import Report

Generated: {now_iso()}

## Requested Source

- repo: `{repo}`
- label: `{label or 'all'}`

## Next Step

Fetch issues through the GitHub connector/MCP tool, then normalize each issue into `.mde/work-items/*.work-item.md`.

"""
    write_text(base / "reports" / "git-issues-import-report.md", report)

    return {
        "status": "prepared",
        "outputs": [".mde/reports/git-issues-import-report.md"],
        "message": "Issue import report created. GitHub issue fetch must be connected through the AI client or GitHub MCP tool.",
    }


@mcp.tool()
def mde_define_work_item(name: str, entity: str = "", operation: str = "", type: str = "change") -> Dict[str, Any]:
    """Define a new MDE work-item and initial plan shell."""
    base = mde_dir()
    slug = slugify(name)
    ensure_dir(base / "work-items")
    ensure_dir(base / "plans")

    work_item_path = base / "work-items" / f"{slug}.work-item.md"
    plan_path = base / "plans" / f"{slug}.plan.md"

    work_item = f"""# Work Item: {name}

Status: draft
Generated: {now_iso()}

## Scope

- type: `{type}`
- entity: `{entity}`
- operation: `{operation}`

## Goal

TBD

## Rules

TBD

## Open Questions

- TBD

"""
    plan = f"""# Plan: {name}

Status: draft
Generated: {now_iso()}

## Work Item

- `.mde/work-items/{slug}.work-item.md`

## Execution Plan

TBD by `mde_review_work_item_scope`.

"""
    write_text(work_item_path, work_item)
    write_text(plan_path, plan)

    return {
        "status": "completed",
        "workItem": f".mde/work-items/{slug}.work-item.md",
        "plan": f".mde/plans/{slug}.plan.md",
        "message": "Work-item and initial plan created.",
    }


@mcp.tool()
def mde_review_work_item_scope(work_item: str) -> Dict[str, Any]:
    """Review work-item scope and produce a planning checkpoint artifact."""
    root = workspace_root()
    base = mde_dir()
    work_item_path = root / work_item
    slug = slugify(work_item_path.stem.replace(".work-item", ""))

    ensure_dir(base / "plans")
    ensure_dir(base / "context")

    if not work_item_path.exists():
        return {"status": "error", "message": f"Work item not found: {work_item}"}

    content = work_item_path.read_text(encoding="utf-8")
    plan_path = base / "plans" / f"{slug}.plan.md"
    files_path = base / "context" / f"{slug}.files.txt"
    submap_path = base / "context" / f"{slug}.submap.json"

    write_text(files_path, "")
    write_json(submap_path, {"generatedAt": now_iso(), "workItem": work_item, "artifacts": []})

    plan = f"""# Plan: {slug}

Status: planned
Generated: {now_iso()}

## Work Item

{work_item}

## Work Item Content

```md
{content[:6000]}
```

## AI Planning Required

The AI should now:

1. read relevant `.mde/models/` files
2. inspect filtered code-map summary
3. identify affected files
4. select skills from `.ai/skills/`
5. complete this plan
6. stop for approval

## Approval

Not approved.

"""
    write_text(plan_path, plan)

    return {
        "status": "completed",
        "plan": f".mde/plans/{slug}.plan.md",
        "context": [
            f".mde/context/{slug}.files.txt",
            f".mde/context/{slug}.submap.json",
        ],
        "message": "Work-item scope reviewed and plan checkpoint created. AI should complete the plan before approval.",
    }


@mcp.tool()
def mde_approve_work_item(plan: str, approved_by: str = "user") -> Dict[str, Any]:
    """Record human approval for a work-item plan."""
    root = workspace_root()
    base = mde_dir()
    plan_path = root / plan
    slug = slugify(plan_path.stem.replace(".plan", ""))
    ensure_dir(base / "approvals")

    if not plan_path.exists():
        return {"status": "error", "message": f"Plan not found: {plan}"}

    approval = {
        "plan": plan,
        "approvedBy": approved_by,
        "approvedAt": now_iso(),
        "status": "approved",
    }
    approval_path = base / "approvals" / f"{slug}.approval.json"
    write_json(approval_path, approval)

    existing = plan_path.read_text(encoding="utf-8")
    if "Status: approved" not in existing:
        existing = existing.replace("Status: planned", "Status: approved")
        existing += f"\n\n## Approval Recorded\n\nApproved by `{approved_by}` at `{approval['approvedAt']}`.\n"
        write_text(plan_path, existing)

    return {
        "status": "approved",
        "approval": f".mde/approvals/{slug}.approval.json",
        "message": "Plan approved. Execution is now allowed.",
    }


@mcp.tool()
def mde_execute_approved_work_item(plan: str, mode: str = "supervised") -> Dict[str, Any]:
    """Execute an approved work-item."""
    root = workspace_root()
    base = mde_dir()
    plan_path = root / plan
    slug = slugify(plan_path.stem.replace(".plan", ""))
    approval_path = base / "approvals" / f"{slug}.approval.json"

    ensure_dir(base / "reports")
    ensure_dir(base / "patches")

    if not plan_path.exists():
        return {"status": "error", "message": f"Plan not found: {plan}"}
    if not approval_path.exists():
        return {"status": "blocked", "message": f"Approval not found: {approval_path}"}

    validation = run_command(["npm", "run", "validate-task"], cwd=root) if (root / "package.json").exists() else {
        "ok": False,
        "stdout": "",
        "stderr": "package.json not found; validation skipped",
    }

    report = f"""# Execution Report: {slug}

Generated: {now_iso()}

## Plan

- `{plan}`

## Mode

- `{mode}`

## Approval

- `{approval_path.relative_to(root)}`

## Validation Result

```json
{json.dumps(validation, indent=2)}
```

## AI IDE Step

The AI IDE should apply only the approved plan, keep changes inside scope, use skills from `.ai/skills/`, and update this report after editing.

"""
    write_text(base / "reports" / f"{slug}.completion-report.md", report)

    return {
        "status": "ready_for_ai_execution",
        "mode": mode,
        "report": f".mde/reports/{slug}.completion-report.md",
        "message": "Approval verified. AI IDE may now execute the approved plan in supervised mode.",
    }


if __name__ == "__main__":
    mcp.run()
