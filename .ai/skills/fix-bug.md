# Skill: Fix Bug Without Architecture Drift

## When to Use

Use this skill when fixing a defect in existing code.

## Required Inputs

- bug description
- failing test or observed behavior
- filtered code-map
- relevant source files
- project-patterns.md

## Steps

1. Reproduce or identify the failure.
2. Use code-map to locate likely affected artifacts.
3. Inspect the exact source code before editing.
4. Determine root cause.
5. Apply the smallest safe fix.
6. Add or update a regression test.
7. Run validation.

## Rules

- Prefer minimal change.
- Preserve existing architecture.
- Do not refactor unrelated code.
- Do not change public contracts unless the bug is in the contract.
- If behavior is ambiguous, document the assumption in the completion report.

## Completion Report

Include:

- root cause
- files changed
- tests added/updated
- validation result
