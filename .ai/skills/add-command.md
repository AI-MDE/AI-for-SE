# Skill: Add Command

## When to Use

Use this skill when the task adds a write operation or use case.

Examples:

- submit leave request
- approve request
- cancel assignment
- create employee

## Required Inputs

- micro-spec
- architecture.md
- app.config.json
- project-patterns.md
- filtered code-map
- nearby source examples

## Steps

1. Read the micro-spec.
2. Identify command name, inputs, rules, outputs, and affected domain objects.
3. Read `architecture.md`.
4. Read `project-patterns.md`.
5. Inspect at least two similar command handlers.
6. Identify affected artifacts:
   - command DTO
   - command handler
   - validator
   - controller/route binding
   - access control policy if needed
   - domain entity/policy changes
   - repository methods
   - tests
7. Apply the smallest consistent change.
8. Do not introduce new architecture patterns unless the micro-spec explicitly requires it.
9. Run build and tests.

## Output Artifacts

Typical files:

```text
src/application/commands/<CommandName>.ts
src/application/commands/<CommandName>Handler.ts
src/presentation/controllers/*
src/domain/*
test/**/*
```

## Checks

Run:

```bash
npm run build
npm test
```

## Forbidden

- Do not put business rules in controllers.
- Do not bypass repositories.
- Do not create transaction logic inconsistently.
- Do not invent a different folder layout.
- Do not make generator code domain-specific to satisfy the task.
