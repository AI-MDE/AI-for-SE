# UC-04: Integrate a Feature into Existing Code

[← Use Cases](../use-cases.md)

## Goal

Add or enhance functionality inside an existing codebase without treating the project as greenfield.

## Actor

Developer / Architect

## Inputs

- feature request
- task scope definition
- selected skill
- code map
- existing source files

## Main Flow

1. AI creates a scoped task definition from the request.
2. Tool filters the code map by module, entity, operation, route, and dependency depth.
3. AI identifies candidate files.
4. AI reads the actual source code.
5. AI identifies local implementation conventions.
6. AI applies a minimal consistent change.
7. Scripts validate build, tests, and task context.
8. Code map is regenerated if needed.

## Diagram

```mermaid
flowchart TD
    A[Feature Request] --> B[AI Creates Task Definition]
    B --> C{Scope Clear?}
    C -- No --> D[AI Surfaces Questions]
    D --> B
    C -- Yes --> E[Select Skill]

    E --> F[Filter Code Map by Scope]
    F --> G[AI Identifies Candidate Files]
    G --> H[AI Reads Source Code]
    H --> I[AI Identifies Local Conventions]
    I --> J[AI Applies Minimal Change]

    J --> K{New Predictable Artifact?}
    K -- Yes --> L[Use Script or Template]
    K -- No --> M[AI Edits Source]

    L --> N[Run Validation]
    M --> N

    N --> O{Pass?}
    O -- No --> P[AI Diagnoses Failure]
    P --> H
    O -- Yes --> Q[Update Code Map if Needed]
    Q --> R[Completion Report]

    subgraph Context
      S[Architecture Guidelines]
      T[Project Patterns]
      U[Skills]
    end

    S --> E
    T --> H
    U --> E
```

## Output

- integrated change
- updated code map when needed
- completion report

## Components Used

Task definition, codebase visibility, architecture and patterns, change coordination, validation mechanism.

---

[← Use Cases](../use-cases.md)
