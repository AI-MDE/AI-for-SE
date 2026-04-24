# Required Components for AI-Assisted Software Engineering

[← Implications](implications.md) | [Next: Problem Statement](problem-statement.md)

Based on the observed gaps and required capabilities, this section outlines the core components an engineer needs in order to effectively use AI in software engineering.

This is not a solution or framework. It is a decomposition of what must exist.

---

## 1. Architectural Guardrails

```text
Define what is allowed and what is not allowed in the system structure.
```

- Layering rules (e.g., controller → service → domain → repository)
- Allowed dependencies
- Cross-cutting concerns (logging, security, transactions)

---

## 2. Project Configuration

```text
Define how the application is structured and organized.
```

- Folder structure
- Naming conventions
- Technology stack choices
- Environment setup

---

## 3. Canonical Patterns

```text
Define how common problems are solved in this project.
```

- CRUD patterns
- Command/query handling
- Validation approach
- Error handling

---

## 4. Task Definition (Scope)

```text
Each change must have a clear, bounded definition.
```

- What is being changed
- What is not being changed
- Expected outcome

---

## 5. Codebase Visibility

```text
The system must provide a way to understand the codebase structure.
```

- File structure
- Relationships between components
- Key entry points

---

## 6. Change Coordination Mechanism

```text
Multi-file changes must be coordinated, not left implicit.
```

- Identify affected components
- Sequence changes
- Ensure consistency across layers

---

## 7. Validation Mechanism

```text
Every change must be verified automatically.
```

- Build validation
- Tests
- Basic consistency checks

---

## 8. Traceability

```text
Link intent to implementation.
```

- Why a change was made
- What was changed
- What validated it

---

## 9. Reusable Execution Patterns

```text
Common engineering tasks should follow repeatable procedures.
```

- Bug fix process
- Feature addition process
- Refactoring process

---

## Summary

```text
The problem is not lack of AI capability.

The problem is the absence of structure around how AI is used.
```

---

## Navigation

[← Implications](implications.md) | [Next: Problem Statement](problem-statement.md)
