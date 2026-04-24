# AI-MDE-Light Diagrams

This page captures the main operating flows for AI-MDE-Light.

## 1. Project AI Initiation for an Existing Codebase

This flow is used when AI-MDE-Light is introduced into an existing software project.

```mermaid
flowchart TD
    A[Existing Codebase] --> B[Run Codebase Analyzer]
    B --> C[Generate Full Code Map]
    C --> D[AI Extracts Project Patterns]
    D --> E[Human Reviews and Normalizes Patterns]
    E --> F[Project Patterns.md]

    G[Architecture Guidance] --> I[AI-MDE-Light Project Context]
    H[App Config] --> I
    F --> I
    C --> I

    I --> J[Create Skills Library]
    J --> K[Define Micro-spec Template]
    K --> L[Ready for Controlled AI-assisted Changes]

    subgraph Inputs
      A
      G
      H
    end

    subgraph Generated_or_Normalized_Artifacts
      C
      F
      J
      K
    end
```

### Purpose

The goal is to convert an existing codebase from implicit knowledge into explicit AI-usable context.

### Output

After initiation, the project should have:

- `.ai/architecture.md`
- `.ai/app.config.json`
- `.ai/project-patterns.md`
- `.ai/skills/*.md`
- `.ai/code-map.full.json`
- `specs/micro-spec.template.md`

---

## 2. Change Request Flow

This flow is used when a user asks for a new feature, fix, enhancement, or integration.

```mermaid
flowchart TD
    A[User Change Request] --> B[AI Converts Request to Micro-spec]
    B --> C{Scope Clear?}
    C -- No --> D[AI Identifies Questions or Assumptions]
    D --> B
    C -- Yes --> E[Select Relevant Skill]

    E --> F[Filter Code Map by Scope]
    F --> G[Create Task Submap]
    G --> H[Identify Candidate Files]
    H --> I[AI Reads Actual Source Files]

    I --> J[Prepare Change Plan]
    J --> K{New Predictable Artifact?}
    K -- Yes --> L[Use Script or Template Generator]
    K -- No --> M[AI Applies Minimal Source Edit]

    L --> N[Run Validation]
    M --> N[Run Validation]

    N --> O{Build and Tests Pass?}
    O -- No --> P[AI Diagnoses Failure]
    P --> I
    O -- Yes --> Q[Update Code Map if Needed]
    Q --> R[Completion Report]

    subgraph Context
      S[Architecture Guidance]
      T[App Config]
      U[Project Patterns]
      V[Skills]
    end

    S --> E
    T --> F
    U --> I
    V --> E
```

### Purpose

The goal is not to let AI freely edit the repo. The goal is to constrain the AI through:

- micro-spec scope
- selected skill
- filtered code-map
- actual source inspection
- validation scripts
- completion report

### Key Principle

```text
Code-map = navigation and impact analysis
Source code = implementation detail
Skills = procedure
Micro-spec = task contract
Scripts = validation and deterministic generation
```
