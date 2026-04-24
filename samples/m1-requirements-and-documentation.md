# M1. Requirements and Documentation — Sample

## Functional Requirements

### REQ-001: Employee Onboarding

**Description:** The system must allow HR administrators to create new employee profiles with mandatory fields and set initial status to Active.

**Acceptance Criteria:**
- First name, last name, email, and role are mandatory
- Email must be unique across all employee records
- System generates a unique ID on creation
- Initial employment status is always Active
- Confirmation is shown after successful creation

**Priority:** High
**Status:** Delivered
**Stakeholder:** HR Operations

---

### REQ-002: Employee Search

**Description:** Users must be able to search and filter employees by name, role, skill, or status.

**Acceptance Criteria:**
- Search supports partial matching on name, role, and skills
- Results can be filtered by employment status
- Results are paginated
- Default sort is by last name ascending

**Priority:** High
**Status:** Delivered
**Stakeholder:** HR Operations, Management

---

## Business Rules

| ID | Rule | Source | Applies To |
|---|---|---|---|
| BR-001 | Each employee must receive a unique system-generated ID | Domain requirement | Employee creation |
| BR-002 | Inactive employees cannot be allocated to new assignments | Business policy | Assignment allocation |
| BR-003 | Profile changes must not erase historical records | Audit requirement | Employee update |

---

## Domain Glossary

| Term | Definition |
|---|---|
| Employee | A consulting staff member whose profile, status, and skills are tracked by the system |
| Onboarding | The process of creating a new employee profile and setting initial status |
| Offboarding | Transitioning an employee to Inactive status |
| Assignment Allocation | Linking an employee to a client project with a role and time period |

---

## Design Decisions

### DD-001: Optimistic Locking for Employee Updates

**Decision:** Use version-based optimistic locking on all employee write operations.
**Rationale:** Multiple HR administrators may edit the same employee concurrently. Pessimistic locking would degrade UX.
**Alternatives Considered:** Last-write-wins (rejected — silent data loss), pessimistic locking (rejected — poor UX).
**Date:** 2026-01-15

---

## API Contracts

### POST /api/employee/onboard

**Request:**
```json
{
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "role": "string",
  "skills": "string",
  "hireDate": "date"
}
```

**Response:**
```json
{
  "id": "uuid",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "role": "string",
  "status": "Active",
  "createdAt": "datetime"
}
```
