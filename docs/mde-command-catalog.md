# MDE Command Catalog

[← Usage Options](usage-options.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)

This page defines the first command set for using AI-MDE from inside an AI-enabled IDE such as Claude Code, Codex, Cursor, or another agentic development environment.

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

## Command List

| Command | Purpose | AI Needed? | Main Output |
|---|---|---:|---|
| `mde_capture_requirements_from_codebase` | Infer draft requirements from existing code | Yes | M1 Requirements draft |
| `mde_capture_architecture_from_codebase` | Infer architecture and patterns from existing code | Yes | M3 Architecture & Patterns draft |
| `mde_generate_codemap` | Generate structural code-map | No | M6 Codebase Model |
| `mde_generate_work_items_from_git_issues` | Convert GitHub issues into work-items | Maybe | Work-item list |
| `mde_define_work_item` | Start a new work-item / plan | Maybe | Work-item draft |
| `mde_review_work_item_scope` | Review scope and develop plan | Yes | Approved-ready plan |
| `mde_approve_work_item` | Approve work-item for execution | Human approval required | Approved plan marker |

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

### Behavior

The command inspects:

- routes/controllers
- command/query handlers
- domain entities
- tests
- README/API docs if available

It produces inferred requirements, not final truth.

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

### Behavior

The command looks for:

- folder/layer structure
- dependency direction
- command/query patterns
- validation patterns
- repository usage
- error handling
- transaction handling
- test structure

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

### Behavior

Runs static analysis over the codebase.

For TypeScript, this can use the TypeScript compiler API or `ts-morph`.

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

### AI Needed?

No. This should be deterministic tooling.

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

### Behavior

The command reads selected GitHub issues and creates structured work-item drafts.

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

### AI Needed?

Maybe.

Fetching issues is deterministic. Converting vague issue text into a structured work-item may require AI.

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

### Behavior

Creates the initial work-item file and captures known scope.

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

### AI Needed?

Maybe.

If scope is explicit, this can be mostly deterministic. If scope is vague, AI helps normalize it.

---

## 6. `mde_review_work_item_scope`

### Purpose

Review work-item scope and develop the execution plan.

This is the main planning checkpoint.

### Invocation

```text
mde_review_work_item_scope workItem=.ai/work-items/approve-leave-request.work-item.md
```

### Behavior

The command:

1. reads the work-item
2. reads relevant models
3. filters the code-map
4. selects applicable skills
5. identifies affected files
6. develops an execution plan
7. stops before execution

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

### AI Needed?

Yes. This requires judgment, scope interpretation, and planning.

---

## 7. `mde_approve_work_item`

### Purpose

Mark a reviewed work-item plan as approved for execution.

This command does **not** execute the change by itself.

It records human approval.

### Invocation

```text
mde_approve_work_item plan=.ai/plans/approve-leave-request.plan.md
```

### Behavior

The command:

- verifies the plan exists
- records approval metadata
- marks the plan as approved
- prepares it for a later execution command

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

### Human Approval Required

Yes. This is the approval gate.

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
```

For day-to-day work, the common path is shorter:

```text
mde_generate_codemap
mde_define_work_item
mde_review_work_item_scope
mde_approve_work_item
```

---

## Approval Boundary

Planning and approval are separate.

```text
review scope / develop plan → human approval → execution allowed
```

No command should apply code changes before the plan is approved.

---

## Possible Future Execution Command

A later execution command may be added:

```text
mde_execute_approved_work_item
```

That command would require:

- approved plan
- selected AI engine
- validation rules
- rollback or patch capture strategy

Until then, `mde_approve_work_item` only approves the plan.

---

## Navigation

[← Usage Options](usage-options.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)
