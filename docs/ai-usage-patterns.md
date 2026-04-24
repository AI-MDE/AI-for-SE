# AI Usage in Real-World Development Scenarios (Market Observation)

[← Intersection](ai-in-software-engineering.md) | [Next: Gaps & Challenges](gaps-and-challenges.md)

This page describes how software engineers use AI tools in common development scenarios, and which capabilities are typically used in each case.

---

## 1. Bug Fixes

### How People Use AI
- Paste error into chat
- Ask for explanation and fix
- Iterate until resolved

### AI Capabilities Commonly Used
- Prompt interfaces
- IDE copilots
- Code-reading tools
- Agents (occasionally)

### Observed Pattern
```text
local problem → prompt → fix → validate
```

---

## 2. Minor Change Requests

### How People Use AI
- Describe change
- Point to file
- Ask AI to follow pattern

### AI Capabilities Commonly Used
- Prompt interfaces
- IDE copilots
- File tools

### Observed Pattern
```text
small edit → pattern reuse → review
```

---

## 3. Significant Enhancements

### How People Use AI
- Break into steps
- Use multiple prompts
- Sometimes plan first

### AI Capabilities Commonly Used
- Prompt interfaces
- Planning modes
- Agents
- Repo tools

### Observed Pattern
```text
decompose → generate → manually coordinate
```

---

## 4. New Applications

### How People Use AI
- Scaffold via prompt
- Add features incrementally

### AI Capabilities Commonly Used
- Prompt interfaces
- Templates
- Copilots

### Observed Pattern
```text
scaffold → extend → patch later
```

---

## 5. Refactoring

### How People Use AI
- Refactor file by file
- Repeat across system

### AI Capabilities Commonly Used
- Prompt interfaces
- Code tools
- Copilots

### Observed Pattern
```text
local refactor → repeat → align manually
```

---

## 6. Documentation

### How People Use AI
- Summarize files
- Generate docs

### AI Capabilities Commonly Used
- Prompt interfaces
- File-reading tools

### Observed Pattern
```text
read → summarize → document
```

---

## Cross-Scenario Insight

```text
Same capabilities are reused, but combined differently each time without consistent structure.
```

---

## Navigation

[← Intersection](ai-in-software-engineering.md) | [Next: Gaps & Challenges](gaps-and-challenges.md)
