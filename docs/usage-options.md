# Usage Options: Applying the Proposed Solution with AI Engines

[← Required Components](required-components.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)

This page describes different ways to apply the proposed structured AI-assisted engineering approach with current AI engines and tools.

The core idea is the same in all options:

```text
persistent project context + scoped task + guided execution + validation
```

The difference is how much of the flow is manual, scripted, integrated, or agent-driven.

---

## Option 1: Plain AI Chat with Structured Inputs

### Description

Use a general AI engine directly, such as ChatGPT, Claude, Gemini, or another model, and manually provide the relevant project context.

### Inputs

- problem statement
- task micro-spec
- architecture guidance
- relevant source files or snippets
- project patterns

### Flow

```text
User gathers context
  → user writes prompt
  → AI proposes plan/code
  → user applies changes
  → user runs validation
```

### Strengths

- easiest to start
- no tooling required
- useful for thinking, review, explanation, and small changes

### Weaknesses

- context must be manually assembled
- easy to omit important files or rules
- no built-in enforcement
- weak repeatability

### Best For

- exploration
- design discussion
- small fixes
- learning the method

---

## Option 2: Skills-Only Approach

### Description

Use skill files as repeatable playbooks that tell the AI how to perform coding tasks.

Example skills:

```text
.ai/skills/add-command.md
.ai/skills/fix-bug.md
.ai/skills/integrate-existing-code.md
.ai/skills/extract-project-patterns.md
```

### Flow

```text
User request
  → select skill
  → provide task scope
  → AI follows playbook
  → user reviews and validates
```

### Strengths

- lightweight
- portable across AI tools
- improves consistency
- easy to version with the repo

### Weaknesses

- still depends heavily on user discipline
- skills can be ignored or misapplied by the AI
- no automatic context discovery unless paired with tools

### Best For

- teams starting from informal AI use
- existing codebases with recognizable patterns
- repeatable coding tasks

---

## Option 3: Commands / CLI-Driven Workflow

### Description

Use repository commands to prepare context, generate code maps, filter scope, and validate task readiness.

Example commands:

```bash
npm run init-ai-mde
npm run analyze
npm run filter-code-map -- --entity LeaveRequest --operation approve
npm run validate-task
```

### Flow

```text
user request
  → micro-spec
  → CLI generates or filters context
  → AI receives scoped context
  → AI edits or proposes changes
  → CLI validates
```

### Strengths

- repeatable
- reduces manual context gathering
- creates a clearer bridge between docs and execution
- makes validation explicit

### Weaknesses

- requires scripts and maintenance
- still needs a human or AI client to apply source changes
- CLI alone does not understand business intent

### Best For

- serious project usage
- existing codebases
- teams that want discipline without building a full platform

---

## Option 4: IDE Agent with Repo Context

### Description

Use an AI coding agent inside an IDE, such as Claude Code, Codex, Cursor, GitHub Copilot, or a similar tool.

The repo provides the agent with:

- architecture guidance
- project patterns
- skills
- micro-specs
- code-map or filtered submap

### Flow

```text
developer opens repo
  → agent reads repo context
  → developer gives scoped task
  → agent inspects files
  → agent edits code
  → developer runs validation
```

### Strengths

- practical for real development
- agent can inspect and edit files
- works naturally with existing source code
- less copy/paste than plain chat

### Weaknesses

- agent behavior varies by tool
- still probabilistic
- may drift without strong repo guidance
- validation must be enforced externally

### Best For

- day-to-day engineering work
- bug fixes
- feature integration
- refactoring with human review

---

## Option 5: MCP-Based Integration

### Description

Expose the structured AI-assisted engineering workflow through an MCP server.

The MCP server can provide tools such as:

```text
get_project_context
get_required_models
generate_code_map
filter_code_map
create_micro_spec
select_skill
validate_task_context
```

### Flow

```text
AI client
  → calls MCP tools
  → retrieves project context
  → filters code-map
  → selects skill
  → proposes or applies change
  → runs validation tools
```

### Strengths

- clean tool boundary
- works across MCP-capable clients
- avoids repeatedly pasting context
- centralizes workflow logic
- good fit for AI-MDE / AI-for-SE methodology

### Weaknesses

- requires server implementation
- tool permissions and client support vary
- must design stable tool contracts

### Best For

- reusable platform direction
- multiple AI clients
- governed workflows
- teams that want a standard integration point

---

## Option 6: Agent-Orchestrated Workflow

### Description

Use an autonomous or semi-autonomous agent to run the full change workflow.

The agent coordinates:

- task interpretation
- model lookup
- code-map filtering
- skill selection
- source inspection
- edit planning
- code modification
- validation
- completion report

### Flow

```text
change request
  → agent creates micro-spec
  → agent filters code-map
  → agent selects skill
  → agent edits files
  → agent runs validation
  → agent reports result
```

### Strengths

- most integrated experience
- lowers developer coordination burden
- can handle multi-step changes
- aligns well with long-term product vision

### Weaknesses

- highest risk if guardrails are weak
- needs strong validation and rollback
- requires careful permission control
- must avoid silent architectural drift

### Best For

- mature environments
- controlled automation
- repeated change workflows
- future productization

---

## Comparison

| Option | Effort | Control | Automation | Best Use |
|---|---:|---:|---:|---|
| Plain AI Chat | Low | Low | Low | Thinking, small tasks |
| Skills Only | Low-Medium | Medium | Low | Repeatable guidance |
| Commands / CLI | Medium | Medium-High | Medium | Project discipline |
| IDE Agent | Medium | Medium | Medium-High | Daily coding |
| MCP Integration | High | High | High | Platform integration |
| Agent-Orchestrated | High | Medium-High | Very High | Mature automation |

---

## Recommended Adoption Path

Start simple and add structure only when needed.

```text
1. Skills only
2. Skills + micro-specs
3. CLI commands + code-map
4. IDE agent using repo context
5. MCP integration
6. Agent-orchestrated workflow
```

This avoids forcing full complexity upfront while still giving a path toward governed automation.

---

## Key Principle

Do not treat these options as competing approaches.

They are maturity levels.

```text
same methodology
  → different execution surfaces
```

The methodology is:

```text
models + scope + skills + code-map + validation
```

The execution surface can be:

```text
chat, skill files, CLI, IDE agent, MCP server, or autonomous agent
```

---

## Navigation

[← Required Components](required-components.md) | [Home](Home.md) | [Next: Use Cases](use-cases.md)
