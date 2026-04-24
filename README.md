# AI-MDE-Light

AI-MDE-Light is a code-first, skill-driven approach to AI-assisted software engineering.

It is not full lifecycle MDE. It keeps the useful discipline of AI-MDE while reducing ceremony for existing codebases, fixes, enhancements, and integrations.

---

## 📚 Documentation (Wiki Style)

Start here:

➡️ [Documentation Home](docs/Home.md)

### Core Pages

- [AI-MDE-Light Overview](docs/ai-mde-light.md)
- [Architecture Guidance](.ai/architecture.md)
- [Project Patterns](.ai/project-patterns.md)
- [Micro-spec Template](specs/micro-spec.template.md)

### Skills

- [.ai/skills/add-command.md](.ai/skills/add-command.md)
- [.ai/skills/fix-bug.md](.ai/skills/fix-bug.md)
- [.ai/skills/extract-project-patterns.md](.ai/skills/extract-project-patterns.md)
- [.ai/skills/integrate-existing-code.md](.ai/skills/integrate-existing-code.md)

### Tools

- [Analyze Codebase](tools/analyze-codebase.ts)
- [Filter Code Map](tools/filter-code-map.ts)
- [Validate Task](tools/validate-task.ts)

---

## Core Idea

```text
User request
  ↓
Micro-spec
  ↓
Skill selection
  ↓
Code-map impact analysis
  ↓
Targeted source inspection
  ↓
AI-assisted edit or script generation
  ↓
Validation
```

## Key Principle

AI should interpret, normalize, plan, and modify carefully.

Scripts should generate predictable artifacts and validate hard rules.

```text
AI      = understand, classify, normalize, edit existing code
Scripts = inspect, generate scaffolds, validate, enforce
Skills  = repeatable engineering playbooks
```

---

## Repository Structure

```text
.ai/
  architecture.md
  app.config.json
  project-patterns.md
  skills/
  templates/
  context/

specs/
  micro-spec.template.md

tools/
  analyze-codebase.ts
  filter-code-map.ts
  validate-task.ts

docs/
  ai-mde-light.md
  Home.md
```

---

## Workflow

1. Capture a small task-level micro-spec.
2. Select the relevant skill.
3. Generate or filter the code-map.
4. Inspect the relevant source files.
5. Apply a minimal change.
6. Run validation.
7. Update the code-map and project patterns when needed.

---

## Modes

### New Code

Use scripts/templates heavily.

```text
micro-spec → generator → new files
```

### Existing Code

Use AI as the adaptive modifier.

```text
micro-spec → code-map → inspect source → AI edit → validation
```

---

## Status

Early architecture starter kit.
