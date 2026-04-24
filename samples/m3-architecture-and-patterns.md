# M3. Architecture and Patterns — Sample

## Architectural Style

Layered architecture with CQRS separation (commands mutate, queries read).

---

## Layering Rules

```
Controller  →  Service / Query Service  →  Domain Entity  →  Repository
```

- Controllers are thin — validate input, delegate to service, return response
- Services contain orchestration logic and business rule enforcement
- Domain entities own state and invariants
- Repositories hide persistence details
- No layer may skip a layer (controller must not call repository directly)

---

## Allowed Dependencies

| Layer | May Depend On |
|---|---|
| Controller | Service, Query Service, DTOs |
| Service | Domain Entity, Repository Interface, DTOs, Validators |
| Query Service | Repository Interface, Read DTOs |
| Domain Entity | Nothing (pure domain) |
| Repository | Domain Entity, Mapper |

---

## Cross-Cutting Concerns

| Concern | Approach |
|---|---|
| Logging | Structured logger injected via context, not imported directly |
| Authentication | Handled at middleware level, context carries identity |
| Authorization | Access control validator per entity, checked before service call |
| Transactions | Service layer owns transaction boundary |
| Error handling | Domain errors thrown as typed exceptions, controller maps to HTTP status |
| Optimistic locking | Version field on mutable aggregate roots, checked at repository level |

---

## Naming Conventions

| Artifact | Pattern | Example |
|---|---|---|
| Domain entity | `{Entity}.entity.ts` | `employee.entity.ts` |
| Service | `{Entity}.service.ts` | `employee.service.ts` |
| Query service | `{Entity}.query-service.ts` | `employee.query-service.ts` |
| Controller | `{Entity}.controller.ts` | `employee.controller.ts` |
| Repository interface | `{Entity}.repository.interface.ts` | `employee.repository.interface.ts` |
| Repository impl | `{Entity}.repository.ts` | `employee.repository.ts` |
| Command DTO | `{action}-{entity}.command.ts` | `onboard-employee.command.ts` |
| Response DTO | `{entity}.response.dto.ts` | `employee.response.dto.ts` |
| Read DTO | `{entity}-read.dto.ts` | `employee-read.dto.ts` |
| Mapper | `{entity}.mapper.ts` | `employee.mapper.ts` |
| Validator | `{entity}.{type}.ts` | `employee.business-rules.ts` |

---

## Canonical Patterns

### Command Handler Pattern

```
Controller receives request
  → validates input (DTO shape)
  → calls access control validator
  → calls state transition validator (if stateful entity)
  → calls business rule validator
  → calls service method
  → service calls repository
  → returns response DTO
```

**Example:** `employee.controller.ts#onboard` → validators → `employee.service.ts#onboard` → `employee.repository.ts`

### Query Pattern

```
Controller receives request
  → calls access control validator
  → calls query service method
  → query service calls repository
  → maps to read DTO
  → returns read DTO
```

**Example:** `employee.controller.ts#search` → `employee.query-service.ts#search` → `employee.repository.ts`

### Composed View Pattern

```
Controller receives request
  → calls service (not query service — composition requires orchestration)
  → service fetches root entity + related data from multiple repositories
  → maps to composed DTO
  → returns composed DTO
```

**Example:** `employee.controller.ts#get360View` → `employee.service.ts#get360View` → multiple repositories

---

## What Is Not Allowed

- Controllers containing business logic
- Direct SQL in service layer
- Cross-module repository access (go through the owning module's service)
- Shared mutable state between requests
- Importing logger directly (use context)
