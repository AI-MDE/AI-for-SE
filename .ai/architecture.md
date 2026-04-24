# Architecture Guidance

These are stable engineering rules for AI-MDE-Light tasks.

## Layering

Use a layered application architecture:

```text
Presentation → Application → Domain → Infrastructure
```

## Presentation Layer

Responsibilities:

- HTTP routing
- request/response mapping
- authentication boundary integration
- input DTO binding
- translating application results to HTTP responses

Rules:

- keep controllers thin
- do not place business rules in controllers
- do not access database directly from controllers

## Application Layer

Responsibilities:

- command handlers
- query handlers
- use-case orchestration
- transaction boundary coordination
- authorization checks
- event dispatching

Rules:

- commands mutate state
- queries read state
- application handlers coordinate, but do not own core business rules

## Domain Layer

Responsibilities:

- entities
- value objects
- policies
- domain services
- invariants
- state transitions

Rules:

- business rules belong here when they represent business truth
- entities should protect their own invariants
- policies should hold reusable decisions

## Infrastructure Layer

Responsibilities:

- repositories
- database access
- external services
- persistence mapping
- messaging implementation

Rules:

- hide persistence behind repository interfaces
- do not leak database-specific details into domain objects

## Request Context

Use a request context object where applicable:

```text
RequestContext:
  - userId
  - roles
  - claims
  - correlationId
  - transaction
```

## Transactions

For write operations:

- define one clear transaction boundary
- ensure all repository writes participate in the same transaction
- do not start nested transactions unless explicitly supported

## Access Control

Prefer explicit access control classes or policies:

```text
EmployeeAccessControl.canDelete(userContext, employee)
```

Use clear return conventions:

- return false/result for expected denial
- throw only for exceptional cases or framework-level enforcement

## Audit

Audit can be implemented through:

- database triggers
- application audit service
- domain/application events

The chosen strategy must be consistent per project.

## Forbidden

- Do not introduce new architecture patterns casually.
- Do not bypass existing repositories.
- Do not put business rules in controllers.
- Do not make generator code domain-specific to fix one request.
