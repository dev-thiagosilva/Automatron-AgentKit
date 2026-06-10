# Jira Ticket Template

Use this template when creating new Jira tickets for this project.

## [Type: Epic / Story] - [Title]

### Summary
[A concise and descriptive summary of the work to be performed.]

---

## If Type is EPIC:

### As-a / I-want / So-what
**As a** [user role/stakeholder],
**I want** [to achieve a specific goal or capability],
**So that** [the value or benefit is realized].

### Stories
* [Story ID].[Number]: [Brief description of the story]
* [...existing code...]

### Blockers / Potential Blockues
- [List any known blockers or risks that might be prevented completion.]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

### Definition of Done (DoD)
- [ ] Code follows `Black` formatting.
- [ ] Code passes `Ruff` linting.
- [ ] Unit tests added/updated and passing.
- [ ] ADR created (if architectural change).

### Reference
- [Link to documentation, ADR, or related PRs]

---

## If Type is STORY:

**Parent Epic:** [epic code]
**Story Points:** [number]

### Description
[Brief description, easy to read and digest, more human like as possible]

### Problem and Solution
[Straight to the point on what the task problem and what will be implemented]

### Impact Analysis
[List any components or modules that might be affected by this change (e.g., `src/agent/graph.py`)]

### Desired path
[Brief description on what the developer can do to succeed the task. A quick guided step by step to developer understand what to do]

### Verification
[Steps to verify the implementation, e.g., "Run `pytest tests/test_feature.py`"]

### Acceptance criteria
- ACC-[number]: [Description]

### Definition of Done (DoD)
- [ ] Code follows `Black` formatting.
- [ ] Code passes `Ruff` linting.
- [ ] Unit tests added/updated and passing.
- [ ] ADR created (if architectural change).

### Reference
- [Link to Epic or related technical docs]
