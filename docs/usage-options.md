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

### How It Is Invoked

There is no tool command. The user manually opens an AI chat and provides structured context.

Example prompt:

```text
I am working in an existing Leave Management codebase.

Use this task scope:
- Add ApproveLeaveRequest
- Manager only
- Requester cannot approve own request
- Only pending requests can be approved

Use these project rules:
- commands handle writes
- domain entity owns state transitions
- repositories handle persistence

Here are the relevant files:
[paste selected files]

Produce a change plan first. Do not write code until the plan is approved.
```

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

### How It Is Invoked

The user references the skill from an AI chat or IDE agent.

Example prompt:

```text
Use .ai/skills/add-command.md.

Task:
Add ApproveLeaveRequest.

Scope:
- entity: LeaveRequest
- operation: approve
- only managers can approve
- requester cannot approve own request
- only pending requests can be approved

Before editing, inspect two similar command handlers and follow the existing pattern.
```

If the AI tool supports custom skills, the skill can be registered with the tool and invoked by name:

```text
/use-skill add-command
Task: Add ApproveLeaveRequest for LeaveRequest approval.
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

Use repository commands or a globally installed `mde` CLI to prepare context, generate code maps, filter scope, and validate task readiness.

### How It Is Invoked: Local Repository Commands

Example local commands:

```bash
npm run init-ai-mde
npm run analyze
npm run filter-code-map -- --entity LeaveRequest --operation approve
npm run validate-task
```

### How It Is Invoked: Global MDE CLI

The preferred AI-MDE product experience is a global install:

```bash
npm install -g @ai-mde/cli
```

Then the user runs:

```bash
mde
```

The CLI displays an interactive menu:

```text
AI-MDE

? What do you want to do?
  1. Initialize project AI context
  2. Generate code-map
  3. Extract project patterns
  4. Create micro-spec
  5. Run change request
  6. Validate task context
  7. Show project status
```

A direct command form is also possible:

```bash
mde init
mde analyze
mde patterns extract
mde spec create --type command --name ApproveLeaveRequest
mde codemap filter --entity LeaveRequest --operation approve
mde change run --spec specs/approve-leave-request.md
mde validate
mde status
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
- gives users a simple entry point: `mde`

### Weaknesses

- requires scripts and maintenance
- still needs a human or AI client to apply source changes unless paired with an agent
- CLI alone does not understand business intent unless connected to an AI engine

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

### How It Is Invoked

First prepare context using the CLI:

```bash
mde analyze
mde codemap filter --entity LeaveRequest --operation approve
```

Then ask the IDE agent:

```text
Use the AI-MDE context for this task.

Read:
- .ai/architecture.md
- .ai/project-patterns.md
- .ai/context/task.submap.json
- .ai/context/task.files.txt
- .ai/skills/add-command.md

Task:
Implement ApproveLeaveRequest from specs/approve-leave-request.md.

Rules:
- inspect candidate files before editing
- apply minimal change
- add/update tests
- run validation after changes
```

With a command-capable IDE agent, the user may simply type:

```text
Run mde change for ApproveLeaveRequest and apply the edits.
```

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

### How It Is Invoked

The MCP server is configured in the AI client.

Example `.vscode/mcp.json` style configuration:

```json
{
  "servers": {
    "mde": {
      "command": "mde-mcp",
      "args": ["--workspace", "."]
    }
  }
}
```

The user asks the AI client:

```text
Use the mde MCP server.
Initialize project context, generate a code-map, and prepare a change request for ApproveLeaveRequest.
```

The AI client calls MCP tools such as:

```text
mde.generate_code_map()
mde.filter_code_map({ entity: "LeaveRequest", operation: "approve" })
mde.select_skill({ taskType: "command" })
mde.validate_task_context()
```

A CLI wrapper can also start the MCP server:

```bash
mde mcp start
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

### How It Is Invoked

Interactive global CLI:

```bash
mde
```

User selects:

```text
? What do you want to do?
  Run change request
```

Then answers prompts:

```text
Change name: ApproveLeaveRequest
Entity: LeaveRequest
Operation: approve
Task type: command
AI engine: claude-code
Apply edits: yes
Run validation: yes
```

Direct command form:

```bash
mde change run \
  --name ApproveLeaveRequest \
  --entity LeaveRequest \
  --operation approve \
  --skill add-command \
  --engine claude-code \
  --apply \
  --validate
```

Expected agent sequence:

```text
1. create or load micro-spec
2. generate or refresh code-map
3. filter code-map
4. select skill
5. inspect source files
6. apply edits
7. run tests/build
8. produce completion report
```

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

| Option | Invocation | Effort | Control | Automation | Best Use |
|---|---|---:|---:|---:|---|
| Plain AI Chat | manual prompt | Low | Low | Low | Thinking, small tasks |
| Skills Only | prompt references skill | Low-Medium | Medium | Low | Repeatable guidance |
| Commands / CLI | `mde` or `npm run ...` | Medium | Medium-High | Medium | Project discipline |
| IDE Agent | IDE prompt + repo context | Medium | Medium | Medium-High | Daily coding |
| MCP Integration | AI calls MCP tools | High | High | High | Platform integration |
| Agent-Orchestrated | `mde change run ...` | High | Medium-High | Very High | Mature automation |

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

## Preferred Product Experience

For AI-MDE, the preferred user experience is:

```bash
npm install -g @ai-mde/cli
mde
```

Then the user chooses from a menu rather than memorizing commands.

Direct commands remain available for automation and scripts.

```bash
mde init
mde analyze
mde patterns extract
mde spec create
mde change run
mde validate
```

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
