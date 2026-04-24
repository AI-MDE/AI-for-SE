# Change Request Worked Example

[← Project Initialization](project-initialization.md) | [Worked Example Home](README.md)

This page shows a complete change request using structured AI-assisted engineering.

This is the cleaned version of the walkthrough: focused, linear, and without initialization overhead.

---

<details open>
<summary><strong>Step 1 — Change Request</strong></summary>

```text
Allow managers to approve or reject leave requests.
```

</details>

---

<details>
<summary><strong>Step 2 — Micro-spec</strong></summary>

```text
Goal:
Allow a manager to approve or reject a leave request.

Inputs:
- leaveRequestId
- managerId
- decision: approve | reject

Rules:
- manager only
- requester cannot approve own request
- cancelled requests cannot be approved
- only pending requests can be changed
```

</details>

---

<details>
<summary><strong>Step 3 — Scope the Codebase</strong></summary>

```bash
npm run filter-code-map -- --entity LeaveRequest --operation approve
```

Outputs:

```text
.ai/context/task.submap.json
.ai/context/task.files.txt
```

</details>

---

<details>
<summary><strong>Step 4 — AI Execution</strong></summary>

Expected AI behavior:

```text
- read micro-spec
- inspect candidate files
- follow architecture and patterns
- apply minimal consistent change
```

Expected artifacts:

```text
- ApproveLeaveRequestHandler
- LeaveRequest.approve()
- LeaveAccessControl.canApprove()
- tests
```

</details>

---

<details>
<summary><strong>Step 5 — Validation</strong></summary>

```bash
npm run validate-task
npm run build
npm test
```

</details>

---

<details>
<summary><strong>Step 6 — Completion Report</strong></summary>

```text
Change:
Approve/reject leave requests

Validated:
build passed
all tests passed
```

</details>

---

## Final Flow

```text
micro-spec → scope → inspect → change → validate
```

---

## Navigation

[← Project Initialization](project-initialization.md) | [Worked Example Home](README.md)
