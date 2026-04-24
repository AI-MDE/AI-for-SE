# Project Patterns

This file should be generated from the existing codebase, then reviewed and normalized by a human.

## Extraction Rule

Only record observed patterns.

For each pattern, include:

- observed examples
- canonical pattern
- inconsistencies
- recommendation

## Controller Pattern

### Observed

_To be extracted._

### Canonical Pattern

- validate/bind request
- call command or query handler
- translate result to HTTP response
- no domain logic

### Inconsistencies

_To be extracted._

## Command Handler Pattern

### Observed

_To be extracted._

### Canonical Pattern

- accept command DTO and RequestContext
- authorize if needed
- load aggregate through repository
- call domain behavior/policy
- save through repository
- return typed result

## Query Handler Pattern

### Observed

_To be extracted._

### Canonical Pattern

- accept query DTO and RequestContext
- call read repository/projection
- return read model
- no mutation

## Repository Pattern

### Observed

_To be extracted._

### Canonical Pattern

- hide persistence
- accept transaction context when needed
- return domain entities or read models according to layer

## Validation Pattern

### Observed

_To be extracted._

## Error Handling Pattern

### Observed

_To be extracted._

## Test Pattern

### Observed

_To be extracted._
