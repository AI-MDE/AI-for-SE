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


@mcp.tool()
def mde_scan_codebase() -> Dict[str, Any]:
    """Scan codebase and generate baseline M4 project configuration and M6 code-map artifacts."""
    root = workspace_root()
    ai_dir = root / ".ai"
    ensure_dir(ai_dir / "models")
    ensure_dir(ai_dir / "reports")

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
    }

    write_json(ai_dir / "models" / "m4-project-configuration.json", project_config)

    analyze_result = run_command(["npm", "run", "analyze"], cwd=root) if package_json.exists() else {
        "ok": False,
        "stdout": "",
        "stderr": "package.json not found; skipped npm run analyze",
    }

    report = f"""# Codebase Scan Summary

Generated: {now_iso()}

## Outputs

- `.ai/models/m4-project-configuration.json`
- `.ai/code-map.full.json` if analyzer succeeded

## Analyzer Result

```text
ok: {analyze_result.get('ok')}
returncode: {analyze_result.get('returncode')}
```

## Notes

This command is artifact-first. Full artifacts are written locally; only this summary is returned to the AI.
"""
    write_text(ai_dir / "reports" / "codebase-scan-summary.md", report)

    return {
        "status": "completed",
        "workspace": str(root),
        "outputs": [
            ".ai/models/m4-project-configuration.json",
            ".ai/reports/codebase-scan-summary.md",
            ".ai/code-map.full.json",
        ],
        "analyzeOk": analyze_result.get("ok"),
        "message": "Codebase scan completed. Large artifacts were written to local files.",
    }


@mcp.tool()
def mde_understand_data_model(source: str = "auto", path: str = "") -> Dict[str, Any]:
    """Inspect database/schema artifacts and create a draft M5 data model."""
    root = workspace_root()
    ai_dir = root / ".ai"
    ensure_dir(ai_dir / "models")
    ensure_dir(ai_dir / "evidence")
    ensure_dir(ai_dir / "reports")

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
    write_json(ai_dir / "evidence" / "data-model-sources.json", evidence)

    draft = f"""# M5 Data Model Draft

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
    write_text(ai_dir / "models" / "m5-data-model.draft.md", draft)
    write_text(ai_dir / "reports" / "data-model-understanding-report.md", draft)

    return {
        "status": "completed",
        "candidateFileCount": len(candidates),
        "outputs": [
            ".ai/evidence/data-model-sources.json",
            ".ai/models/m5-data-model.draft.md",
            ".ai/reports/data-model-understanding-report.md",
        ],
        "message": "Data model evidence collected. AI interpretation should review the generated draft and candidate files.",
    }


@mcp.tool()
def mde_capture_requirements_from_codebase(module: str = "") -> Dict[str, Any]:
    """Create a draft M1 requirements model from codebase evidence."""
    root = workspace_root()
    ai_dir = root / ".ai"
    ensure_dir(ai_dir / "models")
    ensure_dir(ai_dir / "reports")

    code_map = ai_dir / "code-map.full.json"
    draft = f"""# M1 Requirements Draft

Generated: {now_iso()}

## Scope

- module: `{module or 'all'}`

## Evidence

- code-map exists: `{code_map.exists()}`

## AI Interpretation Required

Infer visible features, user actions, business rules, and gaps from controllers, handlers, domain objects, tests, and documentation.

"""
    write_text(ai_dir / "models" / "m1-requirements.draft.md", draft)
    write_text(ai_dir / "reports" / "requirements-capture-report.md", draft)

    return {
        "status": "completed",
        "outputs": [
            ".ai/models/m1-requirements.draft.md",
            ".ai/reports/requirements-capture-report.md",
        ],
        "message": "Requirements draft artifact created. AI should now fill it from selected evidence.",
    }


@mcp.tool()
def mde_capture_architecture_from_codebase(area: str = "") -> Dict[str, Any]:
    """Create a draft M3 architecture and patterns model from codebase evidence."""
    root = workspace_root()
    ai_dir = root / ".ai"
    ensure_dir(ai_dir / "models")
    ensure_dir(ai_dir / "reports")

    draft = f"""# M3 Architecture and Patterns Draft

Generated: {now_iso()}

## Scope

- area: `{area or 'all'}`

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
    write_text(ai_dir / "models" / "m3-architecture-and-patterns.draft.md", draft)
    write_text(ai_dir / "reports" / "architecture-capture-report.md", draft)

    return {
        "status": "completed",
        "outputs": [
            ".ai/models/m3-architecture-and-patterns.draft.md",
            ".ai/reports/architecture-capture-report.md",
        ],
        "message": "Architecture draft artifact created. AI should now fill it from selected evidence.",
    }


@mcp.tool()
def mde_generate_work_items_from_git_issues(repo: str, label: str = "") -> Dict[str, Any]:
    """Create placeholder work-item import report for GitHub issues.

    The actual GitHub fetch should be implemented by the AI client or a GitHub-enabled MCP tool.
    """
    root = workspace_root()
    ai_dir = root / ".ai"
    ensure_dir(ai_dir / "work-items")
    ensure_dir(ai_dir / "reports")

    report = f"""# GitHub Issues Import Report

Generated: {now_iso()}

## Requested Source

- repo: `{repo}`
- label: `{label or 'all'}`

## Next Step

Fetch issues through the GitHub connector/MCP tool, then normalize each issue into `.ai/work-items/*.work-item.md`.

"""
    write_text(ai_dir / "reports" / "git-issues-import-report.md", report)

    return {
        "status": "prepared",
        "outputs": [".ai/reports/git-issues-import-report.md"],
        "message": "Issue import report created. GitHub issue fetch must be connected through the AI client or GitHub MCP tool.",
    }


@mcp.tool()
def mde_define_work_item(name: str, entity: str = "", operation: str = "", type: str = "change") -> Dict[str, Any]:
    """Define a new MDE work-item and initial plan shell."""
    root = workspace_root()
    ai_dir = root / ".ai"
    slug = slugify(name)
    ensure_dir(ai_dir / "work-items")
    ensure_dir(ai_dir / "plans")

    work_item_path = ai_dir / "work-items" / f"{slug}.work-item.md"
    plan_path = ai_dir / "plans" / f"{slug}.plan.md"

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

- `.ai/work-items/{slug}.work-item.md`

## Execution Plan

TBD by `mde_review_work_item_scope`.

"""
    write_text(work_item_path, work_item)
    write_text(plan_path, plan)

    return {
        "status": "completed",
        "workItem": f".ai/work-items/{slug}.work-item.md",
        "plan": f".ai/plans/{slug}.plan.md",
        "message": "Work-item and initial plan created.",
    }


@mcp.tool()
def mde_review_work_item_scope(work_item: str) -> Dict[str, Any]:
    """Review work-item scope and produce a planning checkpoint artifact."""
    root = workspace_root()
    ai_dir = root / ".ai"
    work_item_path = root / work_item
    slug = slugify(work_item_path.stem.replace(".work-item", ""))

    ensure_dir(ai_dir / "plans")
    ensure_dir(ai_dir / "context")

    if not work_item_path.exists():
        return {"status": "error", "message": f"Work item not found: {work_item}"}

    content = work_item_path.read_text(encoding="utf-8")
    plan_path = ai_dir / "plans" / f"{slug}.plan.md"
    files_path = ai_dir / "context" / f"{slug}.files.txt"
    submap_path = ai_dir / "context" / f"{slug}.submap.json"

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

1. read relevant models
2. inspect filtered code-map summary
3. identify affected files
4. select skills
5. complete this plan
6. stop for approval

## Approval

Not approved.

"""
    write_text(plan_path, plan)

    return {
        "status": "completed",
        "plan": f".ai/plans/{slug}.plan.md",
        "context": [
            f".ai/context/{slug}.files.txt",
            f".ai/context/{slug}.submap.json",
        ],
        "message": "Work-item scope reviewed and plan checkpoint created. AI should complete the plan before approval.",
    }


@mcp.tool()
def mde_approve_work_item(plan: str, approved_by: str = "user") -> Dict[str, Any]:
    """Record human approval for a work-item plan."""
    root = workspace_root()
    ai_dir = root / ".ai"
    plan_path = root / plan
    slug = slugify(plan_path.stem.replace(".plan", ""))
    ensure_dir(ai_dir / "approvals")

    if not plan_path.exists():
        return {"status": "error", "message": f"Plan not found: {plan}"}

    approval = {
        "plan": plan,
        "approvedBy": approved_by,
        "approvedAt": now_iso(),
        "status": "approved",
    }
    approval_path = ai_dir / "approvals" / f"{slug}.approval.json"
    write_json(approval_path, approval)

    existing = plan_path.read_text(encoding="utf-8")
    if "Status: approved" not in existing:
        existing = existing.replace("Status: planned", "Status: approved")
        existing += f"\n\n## Approval Recorded\n\nApproved by `{approved_by}` at `{approval['approvedAt']}`.\n"
        write_text(plan_path, existing)

    return {
        "status": "approved",
        "approval": f".ai/approvals/{slug}.approval.json",
        "message": "Plan approved. Execution is now allowed.",
    }


@mcp.tool()
def mde_execute_approved_work_item(plan: str, mode: str = "supervised") -> Dict[str, Any]:
    """Execute an approved work-item.

    This MCP scaffold verifies approval and creates an execution report/checkpoint.
    Actual source edits are performed by the AI IDE using the approved plan.
    """
    root = workspace_root()
    ai_dir = root / ".ai"
    plan_path = root / plan
    slug = slugify(plan_path.stem.replace(".plan", ""))
    approval_path = ai_dir / "approvals" / f"{slug}.approval.json"

    ensure_dir(ai_dir / "reports")
    ensure_dir(ai_dir / "patches")

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

The AI IDE should apply only the approved plan, keep changes inside scope, and update this report after editing.

"""
    write_text(ai_dir / "reports" / f"{slug}.completion-report.md", report)

    return {
        "status": "ready_for_ai_execution",
        "mode": mode,
        "report": f".ai/reports/{slug}.completion-report.md",
        "message": "Approval verified. AI IDE may now execute the approved plan in supervised mode.",
    }


if __name__ == "__main__":
    mcp.run()
