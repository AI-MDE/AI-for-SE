# Skill: Extract Project Patterns

## When to Use

Use this skill to produce or refresh `.ai/project-patterns.md`.

## Goal

Convert implicit codebase conventions into explicit project rules.

## Instructions

Analyze the codebase and extract only observed patterns.

For each pattern:

- list 2-3 concrete examples
- describe the observed pattern
- identify inconsistencies
- recommend the canonical version

## Cover

- folder structure
- controller pattern
- command handler pattern
- query handler pattern
- repository pattern
- validation
- transaction handling
- access control
- error handling
- tests

## Forbidden

- Do not invent patterns not present in code.
- Do not turn one accidental example into a rule.
- Do not hide inconsistencies.
