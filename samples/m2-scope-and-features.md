# M2. Scope / Features — Sample

## Product Overview

**Product:** HR Consulting Staff Management System
**Purpose:** Manage the lifecycle of consulting staff including onboarding, assignments, leave, performance, and client feedback.

---

## Module Boundaries

| Module | Description | Status |
|---|---|---|
| Employee | Staff profiles, onboarding, offboarding, status tracking | Delivered |
| Assignment | Client projects and staffing allocations | Delivered |
| Leave | Absence tracking and approval | Delivered |
| Performance Review | Periodic performance assessments | Delivered |
| Client Feedback | Client satisfaction ratings per employee | Delivered |
| Support Activity | Internal support tasks and time tracking | Delivered |
| Dashboard | Cross-module summaries and KPIs | In Progress |
| Reporting | Export and analytics | Planned |

---

## Feature Inventory

### Employee Module

| Feature | Description | Status | Requirement Ref |
|---|---|---|---|
| Onboard Employee | Create new employee profile | Delivered | REQ-001 |
| Search Employees | Browse, filter, search employee list | Delivered | REQ-002 |
| Employee 360 Profile | Consolidated view with assignments, leave, reviews | Delivered | REQ-004 |
| Edit Profile | Update employee details | Delivered | REQ-005 |
| Offboard Employee | Transition to Inactive | Delivered | REQ-006 |
| Reactivate Employee | Transition back to Active | Delivered | REQ-007 |
| Employee Availability | List employees available for allocation | Delivered | REQ-008 |

### Assignment Module

| Feature | Description | Status | Requirement Ref |
|---|---|---|---|
| Create Assignment | Define a client project | Delivered | REQ-010 |
| Allocate Employee | Assign employee to project with role and dates | Delivered | REQ-011 |
| View Assignment Timeline | Gantt-style view of allocations | Planned | REQ-012 |

---

## What Is Out of Scope

- Payroll and compensation
- Recruitment and hiring pipeline
- External contractor management
- Time and expense tracking (beyond support activities)
- SSO / identity provider integration (uses simple auth)

---

## Milestones

| Milestone | Target | Status |
|---|---|---|
| Core HR (Employee + Assignment + Leave) | 2026-Q1 | Delivered |
| Performance and Feedback | 2026-Q2 | Delivered |
| Dashboard and Reporting | 2026-Q3 | In Progress |
