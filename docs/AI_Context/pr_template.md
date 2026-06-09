# Pull Request Documentation Template

When creating a pull request, please follow this structure so reviewers can quickly understand the intent and impact of your changes.

## Description
Summarize the purpose of the PR in a concise, human‑readable paragraph. Keep it short but informative.

## Link to associated task
[Task name or ticket URL](https://example.com)

## Changes
- **Title** – Brief description of what was changed.
- **Title** – Another change if applicable.

## What Changed
Provide a technical explanation of the modifications. This can include architectural decisions, new dependencies, or refactoring details. Keep it concise but thorough enough for a reviewer to grasp the impact.

## Tests
List any tests added or updated as part of this PR. Include test file names and a short description if necessary.

## Acceptance criteria checklist
- [x] Criterion title – Description (or N/A if not applicable)
- [ ] Another criterion – Description

## Statistics
Run the following command to populate this section:
```bash
python scripts/calculate_elapsed.py
```
Output example:
- **Branch:** feature/my-feature
- **Total commits:** 5
- **Elapsed time:** 3.50 hours

## Screenshots
Attach screenshots if the changes affect UI or visual output. If none, leave this section empty.
