# Change Request Walkthrough (Single Page)

[← Project Initialization](project-initialization.md) | [Worked Example Home](README.md)

This page shows a complete change request from start to finish in one place.

The collapsible sections below act like popup panels.

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
- decision

Rules:
- manager only
- cannot approve own request
- only pending requests can change
```

</details>

---

<details>
<summary><strong>Step 3 — Scope</strong></summary>

```bash
npm run filter-code-map -- --entity LeaveRequest --operation approve
```

</details>

---

<details>
<summary><strong>Step 4 — AI Execution</strong></summary>

```text
read → inspect → apply minimal change
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
<summary><strong>Step 6 — Completion</strong></summary>

```text
Change complete and validated
```

</details>

---

## Flow

```text
micro-spec → scope → inspect → change → validate
```

---

## Navigation

[← Project Initialization](project-initialization.md) | [Worked Example Home](README.md)
