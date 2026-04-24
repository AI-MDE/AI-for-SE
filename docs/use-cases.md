# Use Cases

[← Home](Home.md) | [Next: Diagrams](diagrams.md)

This page defines the initial AI-MDE-Light use cases.

## UC-01: Initiate AI-MDE-Light for an Existing Codebase

### Goal

Prepare an existing codebase so AI can work against it safely and consistently.

### Actor

Developer / Architect

### Inputs

- existing source code
- architecture guidance
- application configuration
- preferred engineering conventions

### Main Flow

1. Run the codebase analyzer.
2. Generate `.ai/code-map.full.json`.
3. Ask AI to extract observed project patterns.
4. Human reviews and normalizes the extracted patterns.
5. Store canonical patterns in `.ai/project-patterns.md`.
6. Confirm or create required skills under `.ai/skills/`.
7. Confirm the micro-spec template.
8. Project is ready for controlled AI-assisted change requests.

### Output

- code-map
- project patterns
- skill library
- micro-spec template
- initialized AI-MDE-Light project context

---

## UC-02: Add a New Command / Use Case

### Goal

Add a write-side application operation using existing architecture and patterns.

### Actor

Developer

### Inputs

- user change request
- micro-spec
- selected skill: `add-command`
- filtered code-map
- relevant source files

### Main Flow

1. AI converts the request into a micro-spec.
2. AI selects the `add-command` skill.
3. Tool filters code-map by entity, operation, and artifact type.
4. AI inspects similar command handlers.
5. AI creates or updates DTO, handler, validator, route binding, domain behavior, repository methods, and tests as needed.
6. Validation scripts run.
7. AI produces a completion report.

### Output

- implemented command
- updated tests
- validation result
- completion report

---

## UC-03: Fix a Bug Without Architecture Drift

### Goal

Fix a defect with minimal change while preserving architecture.

### Actor

Developer

### Inputs

- bug description
- failing behavior or test
- selected skill: `fix-bug`
- filtered code-map
- relevant source files

### Main Flow

1. AI identifies the likely affected area.
2. Tool filters the code-map.
3. AI inspects the source files, not just the map.
4. AI identifies root cause.
5. AI applies the smallest safe fix.
6. AI adds or updates a regression test.
7. Validation runs.
8. AI reports root cause, changed files, and validation result.

### Output

- bug fix
- regression test
- completion report

---

## UC-04: Integrate a Feature into Existing Code

### Goal

Add or enhance functionality inside an existing codebase without treating the project as greenfield.

### Actor

Developer / Architect

### Inputs

- feature request
- micro-spec
- selected integration skill
- code-map
- existing source files

### Main Flow

1. AI creates a micro-spec from the request.
2. Tool filters the code-map by module, entity, operation, route, and dependency depth.
3. AI identifies candidate files.
4. AI reads the actual source code.
5. AI identifies local implementation conventions.
6. AI applies a minimal consistent change.
7. Scripts validate build, tests, and task context.
8. Code-map is regenerated if needed.

### Output

- integrated change
- updated code-map when needed
- completion report

---

## UC-05: Extract or Refresh Project Patterns

### Goal

Convert implicit codebase conventions into explicit AI-usable project patterns.

### Actor

Architect / Senior Developer

### Inputs

- existing codebase
- selected skill: `extract-project-patterns`
- generated code-map

### Main Flow

1. AI scans representative files.
2. AI extracts observed patterns only.
3. AI lists examples for each pattern.
4. AI identifies inconsistencies.
5. AI recommends canonical patterns.
6. Human reviews and approves.
7. `.ai/project-patterns.md` is updated.

### Output

- reviewed project-patterns file
- improved future AI behavior

---

## UC-06: Generate or Filter a Code Map

### Goal

Use static analysis to give AI a scoped view of the codebase.

### Actor

Developer / Tooling Script

### Inputs

- TypeScript source code
- `tools/analyze-codebase.ts`
- `tools/filter-code-map.ts`

### Main Flow

1. Run `npm run analyze`.
2. Generate `.ai/code-map.full.json`.
3. Run `npm run filter-code-map` with task-specific filters.
4. Generate `.ai/context/task.submap.json`.
5. Generate `.ai/context/task.files.txt`.
6. AI uses the filtered submap to decide which source files to inspect.

### Output

- full code-map
- task submap
- candidate file list

---

## Navigation

[← Home](Home.md) | [Next: Diagrams](diagrams.md)
