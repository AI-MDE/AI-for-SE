# Project Initialization Worked Example

[← Worked Example Home](README.md) | [Next: Change Request Example](change-request.md)

This page shows how to initialize structured AI assistance for an existing codebase.

The goal is to prepare the project context before handling individual change requests.

---

<details open>
<summary><strong>Step 1 — Existing Codebase</strong></summary>

We start with an existing Leave Management application.

Current features:

- employees submit leave requests
- managers view pending requests

At this point, the codebase contains useful information, but most of it is implicit:

- folder structure
- naming conventions
- existing implementation patterns
- domain concepts
- test style

The purpose of initialization is to make this implicit knowledge explicit enough for AI to use reliably.

</details>

---

<details>
<summary><strong>Step 2 — Establish Minimal Models</strong></summary>

For project initialization, we do not need every model completed upfront.

The practical starting point is:

```text
M6 Codebase Model
M3 Architecture & Patterns
M4 Project Configuration
```

### M6. Codebase Model

Generated from static analysis.

### M3. Architecture & Patterns

Captured from known rules and observed conventions.

### M4. Project Configuration

Captures stack, folders, commands, and project structure.

</details>

---

<details>
<summary><strong>Step 3 — Run Initialization Commands</strong></summary>

Run:

```bash
npm run init-ai-mde
npm run analyze
```

Expected generated artifact:

```text
.ai/code-map.full.json
```

This code-map is not meant to be read fully by AI every time. It is a tool-facing structure used for filtering and impact analysis.

</details>

---

<details>
<summary><strong>Step 4 — Extract Project Patterns</strong></summary>

Use the project pattern extraction skill:

```text
.ai/skills/extract-project-patterns.md
```

The AI should extract only observed patterns.

For each pattern, it should report:

- concrete examples
- observed convention
- inconsistencies
- recommended canonical pattern

The output becomes:

```text
.ai/project-patterns.md
```

Human review is required. AI extracts; the architect decides.

</details>

---

<details>
<summary><strong>Step 5 — Ready for Change Requests</strong></summary>

After initialization, the project has:

```text
.ai/architecture.md
.ai/app.config.json
.ai/project-patterns.md
.ai/code-map.full.json
.ai/skills/*.md
```

Now change requests can be handled with:

- a micro-spec
- selected skill
- filtered code-map
- source inspection
- validation

</details>

---

## Output of Initialization

The initialized project context allows AI to stop guessing from scratch.

Instead of:

```text
prompt → infer architecture → generate code
```

We now have:

```text
project context → scoped request → skill-guided execution
```

---

## Navigation

[← Worked Example Home](README.md) | [Next: Change Request Example](change-request.md)
