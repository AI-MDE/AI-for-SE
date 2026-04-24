# AI-MDE-Light Architecture

## Purpose

AI-MDE-Light is a pragmatic middle ground between:

- full model-driven generation
- loose AI coding assistance

It assumes many tasks happen against an existing codebase where scripts alone are too weak and unconstrained AI is too risky.

## Main Artifacts

### 1. Architecture Guidance

Stored in:

```text
.ai/architecture.md
```

Defines stable engineering principles.

Examples:

- controllers are thin
- business rules belong in domain entities or policies
- commands mutate state
- queries read state
- repositories hide persistence
- request context carries identity, roles, claims, correlationId, and transaction

### 2. Application Configuration

Stored in:

```text
.ai/app.config.json
```

Defines project-specific paths, stack, commands, and naming conventions.

### 3. Project Patterns

Stored in:

```text
.ai/project-patterns.md
```

Extracted from the existing codebase and reviewed by a human.

It records the official interpretation of how the project already works.

### 4. Skills

Stored in:

```text
.ai/skills/*.md
```

Skills are operational playbooks.

They define how to perform repeatable coding tasks.

### 5. Micro-specs

Stored in:

```text
specs/*.md
```

A micro-spec defines the scope of a single change.

### 6. Code Map

Generated into:

```text
.ai/code-map.full.json
.ai/context/*.submap.json
```

The full code-map is for tools.

Filtered submaps are for AI context.

## Why Code-map and Source Code Both Matter

```text
code-map = navigation and impact analysis
source code = implementation details
```

The AI should not receive the whole source tree when a filtered map can narrow the scope.

## Preferred Task Flow

```text
User request
  ↓
AI creates micro-spec
  ↓
AI selects skill
  ↓
Tool filters code-map
  ↓
AI inspects selected source files
  ↓
AI edits or script generates
  ↓
Validation runs
  ↓
Completion report
```

## Reliability Split

| Concern | Best Owner |
|---|---|
| Interpret messy request | AI |
| Produce micro-spec | AI |
| Discover code structure | Scripts/static analysis |
| Scaffold predictable files | Scripts/templates |
| Modify existing messy code | AI, constrained by skill |
| Validate build/test/layer rules | Scripts |
| Enforce final acceptance | Human + CI |
