# AI Usage Patterns in Software Engineering (Market Observation)

[← Home](Home.md) | [Next: Use Cases](use-cases.md)

This page summarizes how software engineers currently use AI tools in practice, prior to introducing structured approaches.

---

## 1. Direct Prompt-Based Usage

### Description

Engineers interact directly with AI using prompts.

### Observed Behavior

- Iterative prompting
- Trial-and-error refinement
- Frequent copy/paste into IDE
- Re-explaining context repeatedly

### Strengths

- Fast to start
- Flexible
- No setup required

### Limitations

- No persistent structure
- Context lost between interactions
- Inconsistent results
- No traceability

---

## 2. Plan-First Interaction

### Description

Engineers first ask AI for a plan, then execute step-by-step.

### Observed Behavior

- Two-phase interaction (plan → execution)
- Manual tracking of steps

### Strengths

- Improves clarity
- Reduces randomness

### Limitations

- Plans are not enforced
- Execution may drift
- No persistent linkage to code

---

## 3. Tool-Assisted / Agent-Based Usage

### Description

Engineers use tools that operate directly on the codebase and apply changes.

### Observed Behavior

- Multi-file edits
- Automated navigation
- Developer review loop

### Strengths

- Faster for large changes
- Better code awareness

### Limitations

- Implicit decisions
- Architecture inferred, not enforced
- Hard to reproduce behavior

---

## 4. Pattern Imitation

### Description

Engineers ask AI to follow existing code patterns.

### Observed Behavior

- AI scans similar files
- Mimics structure and style

### Strengths

- Aligns with existing code
- Reduces inconsistency

### Limitations

- Replicates bad patterns
- No canonical rules

---

## 5. Observed Pain Points

- Loss of context between tasks
- Inconsistent architecture
- Lack of traceability
- Difficulty scaling across teams
- Hidden AI decisions
- Heavy manual validation

---

## 6. Existing Workarounds

- Breaking tasks into steps
- Writing pseudo-specs in prompts
- Asking AI to follow patterns
- Manually inspecting similar code

These indicate a need for structure and control.

---

## 7. Gap

Current approaches provide speed and flexibility but lack:

- persistent structure
- enforceable workflow
- consistent execution

---

## Key Insight

Engineers are already trying to structure AI usage—but informally.

---

## Navigation

[← Home](Home.md) | [Next: Use Cases](use-cases.md)
