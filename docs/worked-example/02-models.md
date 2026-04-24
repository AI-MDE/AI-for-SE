# 02. Models

[← Starting Context](01-starting-context.md) | [Next: Initialize AI Context](03-initialize-ai-context.md)

This section shows the minimal set of models required to handle the change request.

## M1. Requirements

Managers must be able to approve or reject leave requests.

## M2. Scope

In scope:
- approve leave request
- reject leave request

Out of scope:
- payroll impact
- notifications

## M3. Architecture & Patterns

- commands handle write operations
- domain entity controls state transitions
- access control policy enforces permissions

## M4. Project Configuration

- commands: `src/application/commands`
- domain: `src/domain`
- tests: `test`

## M5. Design & Data Model

Entity: LeaveRequest

Fields:
- id
- employeeId
- status

Operation:
- approve(managerId)

## M6. Codebase Model

Relevant files:
- LeaveRequest.ts
- SubmitLeaveRequestHandler.ts
- LeaveRepository.ts

---

## Navigation

[← Starting Context](01-starting-context.md) | [Next: Initialize AI Context](03-initialize-ai-context.md)
