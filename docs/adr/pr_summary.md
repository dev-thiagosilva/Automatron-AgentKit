# Pull Request Summary

This pull request updates the **Milestone 1: Jira Tickets Plan** with fully detailed Jira tickets following the project’s ticket template. The changes include:

- Added *As‑a / I‑want / So‑what* sections for each story.
- Completed *Desired Path*, *Problem and Solution*, *Impact Analysis*, *Verification*, *Acceptance Criteria*, and a single *Definition of Done* for every ticket.
- Removed duplicate “Definition of Done” entries.
- Ensured all tickets reference the correct epic link.

- Replaced OpenAI integration plan with Ollama local model integration (no-cost).
- Updated `OLLAMA_API_URL` guidance and made `LLM_PROVIDER` default to `ollama` in the plan.
 - Switched default orchestrator from `langchain` to `langgraph` and updated references accordingly.

## Affected Files
- `docs/milestone/milestone_1_plan.md`

## Verification
Run `make format`, `make check`, and `make test` to confirm that the updated plan passes linting, formatting, and unit tests. The file is ready for review.
