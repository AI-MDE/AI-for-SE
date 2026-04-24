# MDE Command Catalog

[← Usage Options](usage-options.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)

This page defines the command set for using AI-MDE from inside an AI-enabled IDE such as Claude Code, Codex, Cursor, or another agentic development environment.

These commands are intended to be **wired and executable**, not future placeholders.

Each command may combine:

- deterministic local scripts
- MCP tool calls
- AI reasoning steps
- local artifact writes
- short AI-visible summaries

---

## Naming Convention

Terminal commands use:

```bash
> mde ...
```

AI IDE commands use:

```text
mde_<command>
```

This catalog focuses on the AI IDE command form.

---

## Command Principle

MDE commands are **artifact-first**.

They write durable local files and return only short AI-visible summaries unless the AI explicitly needs selected context.

```text
large output → local files
small summary → AI context
```

This keeps token usage low and avoids sending large generated artifacts back to the model unnecessarily.

---

## MCP Execution Model

The AI IDE command is the user-facing command.

Behind it, the AI client may call MCP tools that wrap local scripts.

Example:

```text
mde_generate_codemap
  → MCP tool: mde.generate_codemap
  → local script: mde analyze
  → output: .ai/code-map.full.json
  → AI-visible summary only
```

The core rule:

```text
Scripts do deterministic work.
AI does interpretation, normalization, planning, and code editing.
MCP connects the AI IDE to the local MDE toolchain.
```

---

## Command List

| Command | Purpose | Script Step | AI Step | Main Output |
|---|---|---|---|---|
| `mde_capture_requirements_from_codebase` | Infer draft requirements from existing code | collect routes, handlers, tests, docs | infer requirements and gaps | M1 Requirements draft |
| `mde_capture_architecture_from_codebase` | Infer architecture and patterns from existing code | collect structure, dependencies, examples | normalize architecture and patterns | M3 Architecture & Patterns draft |
| `mde_generate_codemap` | Generate structural code-map | static analysis | none, except summary interpretation | M6 Codebase Model |
| `mde_generate_work_items_from_git_issues` | Convert GitHub issues into work-items | fetch issues | normalize vague issues into work-items | Work-item list |
| `mde_define_work_item` | Start a new work-item / plan | create work-item artifact | normalize scope if needed | Work-item draft |
| `mde_review_work_item_scope` | Review scope and develop plan | load models, filter code-map | plan affected changes | Approved-ready plan |
| `mde_approve_work_item` | Approve work-item for execution | record approval metadata | none, approval is human | Approved plan marker |
| `mde_execute_approved_work_item` | Execute approved work-item | load approved plan, run validation | apply changes through AI IDE | changed files + report |

---

## 1. `mde_capture_requirements_from_codebase`

### Purpose

Capture draft requirements from an existing codebase.

This is useful when a project has working code but poor or missing requirements documentation.

### Invocation

```text
mde_capture_requirements_from_codebase
```

Optional scoped invocation:

```text
mde_capture_requirements_from_codebase module=leave-management
```

### MCP / Script Steps

```text
mde.scan_routes
mde.scan_handlers
mde.scan_domain_entities
mde.scan_tests
mde.collect_existing_docs
```

These steps write extracted evidence to local files:

```text
.ai/evidence/routes.json
.ai/evidence/handlers.json
.ai/evidence/domain-entities.json
.ai/evidence/tests.json
.ai/evidence/docs-index.json
```

### AI Steps

The AI reads the evidence summaries and produces inferred requirements:

```text
- identify visible features
- infer user actions
- infer business rules from tests and domain code
- mark confidence level
- mark gaps and assumptions
```

### File Outputs

```text
.ai/models/m1-requirements.draft.md
.ai/reports/requirements-capture-report.md
```

### AI-visible Response

```text
Requirements draft created.
Output: .ai/models/m1-requirements.draft.md
Confidence: draft / requires human review
```

### Human Review Required

Yes. AI is inferring intent from implementation, so the result must be reviewed.

---

## 2. `mde_capture_architecture_from_codebase`

### Purpose

Capture architecture rules and observed project patterns from an existing codebase.

This is used to build or refresh M3 Architecture & Patterns.

### Invocation

```text
mde_capture_architecture_from_codebase
```

Optional scoped invocation:

```text
mde_capture_architecture_from_codebase area=application-layer
```

### MCP / Script Steps

```text
mde.scan_folders
mde.scan_import_graph
mde.find_pattern_examples
mde.scan_tests
mde.scan_config
```

These steps write evidence files:

```text
.ai/evidence/folder-structure.json
.ai/evidence/import-graph.json
.ai/evidence/pattern-examples.json
.ai/evidence/test-structure.json
.ai/evidence/project-config.json
```

### AI Steps

The AI reviews the evidence and creates a draft architecture/pattern model:

```text
- identify layers
- identify dependency direction
- identify common handler/controller/repository patterns
- identify inconsistencies
- recommend canonical patterns
```

### File Outputs

```text
.ai/models/m3-architecture-and-patterns.draft.md
.ai/reports/architecture-capture-report.md
```

### AI-visible Response

```text
Architecture and patterns draft created.
Output: .ai/models/m3-architecture-and-patterns.draft.md
Review needed: yes
```

### Human Review Required

Yes. The AI extracts and normalizes, but the architect decides what becomes canonical.

---

## 3. `mde_generate_codemap`

### Purpose

Generate a structural model of the existing codebase.

This is M6 Codebase Model.

### Invocation

```text
mde_generate_codemap
```

Equivalent terminal form:

```bash
> mde analyze
```

### MCP / Script Steps

```text
mde.generate_codemap
```

Equivalent local script:

```bash
> mde analyze
```

For TypeScript, this can use the TypeScript compiler API or `ts-morph`.

### AI Steps

No AI is required to generate the code-map.

The AI may only read the short summary to decide the next command.

### File Outputs

```text
.ai/code-map.full.json
.ai/reports/code-map-summary.md
```

### AI-visible Response

```text
Code-map generated.
Files scanned: 214
Artifacts found: 482
Output: .ai/code-map.full.json
```

---

## 4. `mde_generate_work_items_from_git_issues`

### Purpose

Generate new MDE work-items from GitHub issues.

This converts external issue tracking into structured planning artifacts.

### Invocation

```text
mde_generate_work_items_from_git_issues repo=AI-MDE/AI-for-SE
```

Optional filters:

```text
mde_generate_work_items_from_git_issues repo=AI-MDE/AI-for-SE label=enhancement
```

### MCP / Script Steps

```text
mde.github_fetch_issues
mde.github_fetch_issue_comments
mde.create_work_item_files
```

### AI Steps

The AI normalizes each issue into a work-item:

```text
- summarize intent
- identify scope
- classify type: bug, feature, refactor, docs, infrastructure
- identify missing information
- suggest related models
```

### File Outputs

```text
.ai/work-items/<issue-number>-<slug>.work-item.md
.ai/reports/git-issues-import-report.md
```

### AI-visible Response

```text
Generated 4 work-item drafts from GitHub issues.
Output folder: .ai/work-items/
```

---

## 5. `mde_define_work_item`

### Purpose

Define a new work-item and start a new plan.

A work-item is the controlled unit of change.

### Invocation

```text
mde_define_work_item name=ApproveLeaveRequest
```

With scope:

```text
mde_define_work_item name=ApproveLeaveRequest entity=LeaveRequest operation=approve type=command
```

### MCP / Script Steps

```text
mde.create_work_item
mde.create_initial_plan
mde.link_models
```

### AI Steps

If the scope is vague, the AI normalizes it:

```text
- clarify goal
- identify task type
- identify likely model impact
- identify open questions
- draft initial micro-spec
```

### File Outputs

```text
.ai/work-items/approve-leave-request.work-item.md
.ai/plans/approve-leave-request.plan.md
```

### AI-visible Response

```text
Work-item created.
Plan started.
Next: run mde_review_work_item_scope
```

---

## 6. `mde_review_work_item_scope`

### Purpose

Review work-item scope and develop the execution plan.

This is the main planning checkpoint.

### Invocation

```text
mde_review_work_item_scope workItem=.ai/work-items/approve-leave-request.work-item.md
```

### MCP / Script Steps

```text
mde.load_work_item
mde.load_models
mde.filter_codemap
mde.select_candidate_files
mde.select_skills
```

### AI Steps

The AI develops the plan:

```text
- inspect work-item scope
- review relevant model context
- inspect filtered code-map summary
- identify affected files
- identify affected models
- produce implementation plan
- mark risks and assumptions
- stop before execution
```

### File Outputs

```text
.ai/plans/approve-leave-request.plan.md
.ai/context/approve-leave-request.submap.json
.ai/context/approve-leave-request.files.txt
```

### AI-visible Response

```text
Scope reviewed.
Plan created.
Approval required before execution.
Output: .ai/plans/approve-leave-request.plan.md
```

---

## 7. `mde_approve_work_item`

### Purpose

Mark a reviewed work-item plan as approved for execution.

This records human approval and enables execution.

### Invocation

```text
mde_approve_work_item plan=.ai/plans/approve-leave-request.plan.md
```

### MCP / Script Steps

```text
mde.verify_plan_exists
mde.verify_plan_status
mde.record_approval
mde.mark_plan_approved
```

### AI Steps

No AI reasoning is required.

The human approval is the important action.

### File Outputs

```text
.ai/plans/approve-leave-request.plan.md
.ai/approvals/approve-leave-request.approval.json
```

### AI-visible Response

```text
Plan approved.
Execution is now allowed.
Approved by: <user>
```

---

## 8. `mde_execute_approved_work_item`

### Purpose

Execute an approved work-item using the selected AI IDE and local MDE toolchain.

This command is not a future placeholder. It is part of the intended wired workflow.

Execution is allowed only after `mde_approve_work_item` records approval.

### Invocation

```text
mde_execute_approved_work_item plan=.ai/plans/approve-leave-request.plan.md
```

Optional:

```text
mde_execute_approved_work_item plan=.ai/plans/approve-leave-request.plan.md mode=supervised
```

### MCP / Script Steps

```text
mde.verify_approval
mde.load_approved_plan
mde.load_candidate_files
mde.load_selected_skills
mde.create_patch_checkpoint
mde.run_validation
```

### AI Steps

The AI IDE performs the adaptive source change:

```text
- read approved plan
- inspect candidate files
- apply only approved changes
- keep changes inside approved scope
- update tests
- run validation
- if validation fails, propose fix or stop
- produce completion report
```

### File Outputs

```text
.ai/reports/approve-leave-request.completion-report.md
.ai/patches/approve-leave-request.patch
```

### AI-visible Response

```text
Approved work-item executed.
Validation completed.
Completion report: .ai/reports/approve-leave-request.completion-report.md
```

### Safety Rule

If the actual implementation requires changes outside the approved plan, the command must stop and request plan revision.

---

## Suggested Workflow

```text
mde_capture_requirements_from_codebase
mde_capture_architecture_from_codebase
mde_generate_codemap
mde_generate_work_items_from_git_issues
mde_define_work_item
mde_review_work_item_scope
mde_approve_work_item
mde_execute_approved_work_item
```

For day-to-day work, the common path is shorter:

```text
mde_generate_codemap
mde_define_work_item
mde_review_work_item_scope
mde_approve_work_item
mde_execute_approved_work_item
```

---

## Approval Boundary

Planning, approval, and execution are separate.

```text
define work-item → review scope / develop plan → human approval → execute approved plan → validate
```

No command should apply code changes before the plan is approved.

---

## Command State Model

```text
work-item: draft
  → scoped
  → planned
  → approved
  → executed
  → validated
```

Each command moves the work-item forward one controlled step.

---

## Navigation

[← Usage Options](usage-options.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)
