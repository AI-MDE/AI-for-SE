# AI Usage in Real-World Development Scenarios (Market Observation)

[← Home](Home.md) | [Next: Use Cases](use-cases.md)

This page describes how software engineers actually use AI tools in common development scenarios, and where those approaches succeed or break down.

The goal is to observe current behavior before introducing any proposed solution.

---

## 1. Bug Fixes

### Typical Scenario

A developer needs to fix a defect in existing code.

Examples:

```text
- API returns the wrong status code
- validation rule is not applied
- calculation produces the wrong result
- test is failing
```

### How AI Is Used

Engineers usually:

- paste the error message or failing test
- ask AI to explain the cause
- ask AI to patch the specific function or file
- rerun tests manually
- repeat until the failure is gone

### What Works

- AI is good at explaining errors
- AI can quickly identify likely causes
- AI can produce small local fixes
- Works well when the bug is isolated

### Where It Breaks

- AI may fix the symptom, not the cause
- local fixes can violate broader patterns
- hidden dependencies may be missed
- regression tests are often skipped unless requested

### Key Observation

```text
Bug fixing works best when the problem is local and reproducible.
```

---

## 2. Minor Change Requests

### Typical Scenario

A developer needs to make a small controlled change.

Examples:

```text
- add a field to a DTO
- add a validation rule
- rename a label
- add one route parameter
- adjust a query filter
```

### How AI Is Used

Engineers usually:

- describe the change in a short prompt
- point AI to the relevant file
- ask it to follow nearby patterns
- manually review the diff

### What Works

- Very fast turnaround
- Good use of local context
- Low setup cost
- Useful for repetitive edits

### Where It Breaks

- related files may be missed
- tests may not be updated
- naming or layering may drift
- change scope may expand unintentionally

### Key Observation

```text
Minor changes are where current AI tools feel most productive, but still rely heavily on developer review.
```

---

## 3. Significant Enhancement / Adding New Scope

### Typical Scenario

A developer needs to add a feature that touches multiple parts of the system.

Examples:

```text
- add approval workflow
- add a new module
- add reporting functionality
- introduce a new business rule across several operations
```

### How AI Is Used

Engineers typically:

- break the feature into smaller tasks
- use prompts for each step
- ask AI to follow existing patterns
- manually identify affected files
- sometimes ask AI for a plan first

### What Works

- Fast generation of individual components
- Good reuse of local patterns
- Useful for incremental development

### Where It Breaks

- no reliable coordination across files
- dependencies are handled manually
- architecture decisions become inconsistent
- no unified view of the whole change

### Key Observation

```text
AI can generate pieces of a feature, but developers still coordinate the whole change.
```

---

## 4. Building a New Application

### Typical Scenario

A developer starts a new system from scratch.

### How AI Is Used

Engineers usually:

- start with high-level prompts
- ask for scaffolding
- generate features incrementally
- ask for plans when complexity increases
- patch inconsistencies as the system grows

### What Works

- Very fast initial scaffolding
- Rapid experimentation
- Low barrier to entry

### Where It Breaks

- early decisions are ad hoc
- structure drifts over time
- no persistent architecture model
- refactoring becomes inevitable

### Key Observation

```text
AI accelerates the first version, but does not guarantee long-term coherence.
```

---

## 5. Refactoring an Existing Application

### Typical Scenario

A developer improves structure without changing behavior.

Examples:

```text
- split large service classes
- move business logic out of controllers
- introduce repositories
- standardize error handling
```

### How AI Is Used

Engineers usually:

- select a file or function
- ask AI to refactor it
- repeat across files
- manually ensure consistency
- rerun tests after each step

### What Works

- Good for local cleanup
- Speeds up repetitive refactoring
- Helps modernize old code

### Where It Breaks

- no global coordination
- hidden dependencies may be missed
- inconsistent patterns may be introduced
- behavior preservation is hard to prove

### Key Observation

```text
Refactoring requires global understanding, but AI tools often operate locally or heuristically.
```

---

## 6. Documenting an Existing Application

### Typical Scenario

A developer needs to understand or document an existing codebase.

### How AI Is Used

Engineers usually:

- ask AI to summarize files
- generate README content
- explain modules and flows
- create onboarding notes

### What Works

- Fast high-level summaries
- Useful onboarding aid
- Helps expose structure in unfamiliar code

### Where It Breaks

- documentation reflects code, not necessarily intent
- generated docs can become stale quickly
- links between docs and code are weak
- module-level documentation may be inconsistent

### Key Observation

```text
AI can describe a system, but does not automatically maintain a living documentation model.
```

---

## Cross-Scenario Usage Patterns

Across all scenarios, engineers commonly use AI through:

- direct prompts
- plan-first prompting
- IDE copilots
- agent-style tools
- pattern imitation from existing code
- manual review and correction

These are practical adaptations to the limits of current tools.

---

## Core Limitations Observed

### 1. No Persistent Structure

Decisions are often reconstructed task by task.

### 2. Weak Coordination

Multi-file and multi-step changes are manually managed.

### 3. Implicit Decisions

AI makes choices about structure, naming, and behavior without always exposing why.

### 4. No Strong Traceability

Intent, implementation, and validation are not consistently connected.

### 5. Manual Consistency Enforcement

Developers remain responsible for ensuring architectural alignment.

---

## Key Observation

```text
AI is effective at generating and modifying parts of a solution,
but developers still supply most of the structure, coordination, and validation.
```

---

## Navigation

[← Home](Home.md) | [Next: Use Cases](use-cases.md)
