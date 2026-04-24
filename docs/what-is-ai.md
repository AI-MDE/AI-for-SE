# What Is AI (in This Context)

[← Home](Home.md) | [Next: Software Engineering](what-is-software-engineering.md)

For this repository, “AI” refers to large language model (LLM) systems used to:

- generate code and text
- explain and transform existing code
- search and summarize repositories
- propose multi-step changes

## Properties Relevant to Engineering

- Probabilistic output (not guaranteed correctness)
- Context-bound (limited working memory per interaction)
- Pattern-driven (learns from examples, not explicit rules)
- Stateless by default (no durable memory unless engineered)

## Common AI Vendor Assets

| Asset | Brief Definition | How It Helps Software Engineering |
|---|---|---|
| Prompts | Natural-language instructions given to the AI | Quick task execution, explanation, code generation, and troubleshooting |
| Skills | Reusable task playbooks or instructions | Standardizes how AI performs repeated engineering tasks |
| Tools | Functions the AI can invoke, such as file reads, searches, or commands | Lets AI inspect code, run checks, or perform controlled actions |
| MCP Servers | External tool/resource servers exposed to AI clients | Connects AI to repositories, databases, CLIs, docs, and custom engineering systems |
| Plugins / Connectors | Integrations with external services | Gives AI access to systems like GitHub, Google Drive, email, or project tools |
| Agents | AI workflows that can plan, act, observe, and retry | Supports multi-step changes across files or tasks |
| Memory / Context Files | Persistent project guidance or saved context | Helps preserve conventions, architecture decisions, and project-specific rules |

## Implication

```text
AI is excellent at producing and transforming artifacts,
but does not inherently enforce structure, consistency, or continuity.
```

## Navigation

[← Home](Home.md) | [Next: Software Engineering](what-is-software-engineering.md)
