# AI Usage in Real-World Development Scenarios

[← Intersection](ai-in-software-engineering.md) | [Next: Gaps & Challenges](gaps-and-challenges.md)

This page describes how software engineers commonly use AI tools across development scenarios, and which capabilities are typically involved.

Capability names match the table in [What Is AI](what-is-ai.md#common-ai-capabilities).

---

## 1. Bug Fixes

### How Engineers Use AI
- Paste error message or stack trace into a prompt
- Ask for explanation and suggested fix
- Iterate until the fix compiles and tests pass

### Capabilities Commonly Used
- Prompts, Tools (file reads, search), Agents (occasionally)

### Observed Pattern
```text
local problem -> prompt -> fix -> validate
```

### What typically works
Small, well-isolated bugs with clear error messages.

### Where it breaks down
Bugs that span multiple files or layers. Context is reconstructed from scratch each time, so the AI may miss related code.

---

## 2. Minor Change Requests

### How Engineers Use AI
- Describe the change in natural language
- Point to the relevant file or area
- Ask AI to follow existing patterns

### Capabilities Commonly Used
- Prompts, Tools (file reads)

### Observed Pattern
```text
small edit -> pattern reuse -> review
```

### What typically works
Single-file changes where the surrounding pattern is obvious.

### Where it breaks down
When the change touches shared types, configuration, or conventions the AI cannot see.

---

## 3. Significant Enhancements

### How Engineers Use AI
- Break the feature into steps
- Use multiple prompts across files
- Sometimes plan the approach first

### Capabilities Commonly Used
- Prompts, Agents, Tools (file reads, search), Memory/Context Files

### Observed Pattern
```text
decompose -> generate -> manually coordinate
```

### What typically works
Well-defined features where the developer provides structure upfront.

### Where it breaks down
Multi-file coordination. The AI generates each piece in isolation; the developer manually stitches them together and resolves inconsistencies.

---

## 4. New Applications

### How Engineers Use AI
- Scaffold via prompt or template
- Add features incrementally

### Capabilities Commonly Used
- Prompts, Agents, Skills (templates)

### Observed Pattern
```text
scaffold -> extend -> patch later
```

### What typically works
Getting a running skeleton quickly.

### Where it breaks down
The initial scaffold makes assumptions about architecture, naming, and layering that are difficult to change later. Patching accumulates.

---

## 5. Refactoring

### How Engineers Use AI
- Refactor file by file
- Repeat the same transformation across the system

### Capabilities Commonly Used
- Prompts, Tools (search, file reads)

### Observed Pattern
```text
local refactor -> repeat -> align manually
```

### What typically works
Mechanical, well-scoped refactors (rename, extract, inline).

### Where it breaks down
System-wide refactors where consistency matters. Without a global view, the AI applies the refactor differently in different places.

---

## 6. Documentation

### How Engineers Use AI
- Summarize files or modules
- Generate docs from code

### Capabilities Commonly Used
- Prompts, Tools (file reads)

### Observed Pattern
```text
read -> summarize -> document
```

### What typically works
Explaining what code does right now.

### Where it breaks down
Documentation disconnects from implementation over time. The AI summarizes a snapshot; it does not maintain a living document.

---

## Cross-Scenario Insight

```text
The same capabilities are reused across scenarios,
but combined differently each time without consistent structure.

The gap is not in AI capability—it is in the absence of
persistent structure around how that capability is applied.
```

---

## Navigation

[← Intersection](ai-in-software-engineering.md) | [Next: Gaps & Challenges](gaps-and-challenges.md)
