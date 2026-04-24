# 04. Change Request

[← Initialize AI Context](03-initialize-ai-context.md) | [Next: Validation](05-validation.md)

## Micro-spec

```text
Goal: Approve or reject leave request

Inputs:
- leaveRequestId
- managerId
- decision

Rules:
- manager only
- cannot approve own request
- status transition enforced
```

## Execution

```bash
npm run run-change
```

---

## Navigation

[← Initialize AI Context](03-initialize-ai-context.md) | [Next: Validation](05-validation.md)
