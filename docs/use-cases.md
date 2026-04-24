# Use Cases

[← Required Components](required-components.md) | [Home](Home.md)

This section defines use cases for structured AI-assisted engineering. Each use case maps to one or more [required models](required-components.md).

---

| # | Use Case | Actor | Models | Summary |
|---|---|---|---|---|
| UC-00 | [Capture Requirements and Scope](use-cases/uc-00-capture-requirements-and-scope.md) | PO / BA / Architect | M1, M2, M5 | Establish and refine requirements, documentation, and project scope |
| UC-01 | [Define Architecture, Patterns, and Guidelines](use-cases/uc-01-define-architecture-guidelines.md) | Architect / Tech Lead | M3 | Establish architecture guidelines and extract canonical patterns |
| UC-02 | [Initialize AI Context](use-cases/uc-02-initialize-ai-context.md) | Developer / Architect | M4, M6 | Generate code map, assemble project context, prepare for controlled changes |
| UC-03 | [Fix a Bug](use-cases/uc-03-fix-bug.md) | Developer | M6 | Fix a defect with minimal change while preserving architecture |
| UC-04 | [Integrate a Feature](use-cases/uc-04-integrate-feature.md) | Developer / Architect | M1, M2, M5, M6 | Add or enhance functionality without treating the project as greenfield |

---

## Suggested Order

UC-00, UC-01, and UC-02 are prerequisites — run them when introducing structured AI assistance to a project. All three are ongoing: requirements, patterns, and the code map evolve as the system changes. UC-03 and UC-04 are operational use cases invoked as needed during development.

---

## Navigation

[← Required Components](required-components.md) | [Home](Home.md)
