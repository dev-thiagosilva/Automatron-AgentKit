# Milestone 1: Jira Tickets Plan

This document outlines the breakdown of Epics into actionable Jira tickets for Milestone 1. Each ticket is designed to be implemented in a single branch and finalized with a single Pull Request (PR), followed by an Architecture Decision Record (ADR).

## Epic 1: Add a Simple AI Chatbot
**Goal:** Transition from mock nodes to real LLM integration (OpenAI & Ollama) and ensure end-to-end flow.

## CHAT-1: Implement OpenAI Integration in Researcher Node

[Type: Story] - Implement OpenAI Integration in Researcher Node

### Summary
Add support for OpenAI LLM in the Researcher node using `langchain_openai`, configuring API keys via environment variables.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
5

#### Description
The current Researcher node uses mock responses. This ticket replaces the mock with real OpenAI calls by integrating `langchain_openai`. The implementation will:
- Import and configure `OpenAI` from langchain.
- Read `OPENAI_API_KEY` from environment variables.
- Update the graph to use the new LLM provider.

#### Problem and Solution
Problem: No real LLM integration, limiting end‑to‑end testing. 
Solution: Replace mock with OpenAI calls via langchain.

#### Impact Analysis
`src/agent/graph.py`, `src/agent/state.py` (if provider tracking needed).

#### Desired Path
1. Add `langchain_openai` to requirements.
2. Update node implementation.
3. Write unit tests for OpenAI integration.

#### Verification
Run `pytest tests/test_graph.py` and ensure the Researcher node returns real responses.

#### Acceptance Criteria
- AC-1: The Researcher node uses `langchain_openai`.
- AC-2: API key is read from `OPENAI_API_KEY` env var.
- AC-3: Unit tests pass with mocked OpenAI responses.

#### Definition of Done (DoD)
- Code follows Black formatting.
- Code passes Ruff linting.
- Unit tests added/updated and passing.
- ADR created if architectural change is significant.

#### Reference
[Epic 1](docs/milestone/milestone_1_plan.md#epic-1-add-a-simple-ai-chatbot)

## CHAT-2: Implement Ollama Integration in Writer Node

[Type: Story] - Implement Ollama Integration in Writer Node

### Summary
Add support for local LLM via Ollama in the Writer node, enabling provider switching.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
5

#### Description
Update the Writer node to call an Ollama endpoint using `langchain_ollama`. The graph should be configurable to use either OpenAI or Ollama based on environment variables.

#### Problem and Solution
Problem: Only OpenAI is supported, limiting local testing. 
Solution: Integrate Ollama provider via langchain.

#### Impact Analysis
`src/agent/graph.py`, `src/agent/state.py` (provider config).

#### Desired Path
1. Add `langchain_ollama` to requirements.
2. Implement Ollama LLM class.
3. Update graph configuration logic.
4. Write tests for local LLM path.

#### Verification
Run `pytest tests/test_graph.py` ensuring Writer node can use Ollama.

#### Acceptance Criteria
- AC-1: Writer node uses Ollama when configured.
- AC-2: Provider selection via env var `LLM_PROVIDER`.
- AC-3: Tests pass with mocked Ollama responses.

#### Definition of Done (DoD)
- Code follows Black formatting.
- Code passes Ruff linting.
- Unit tests added/updated and passing.
- ADR created if architectural change is significant.

#### Reference
[Epic 1](docs/milestone/milestone_1_plan.md#epic-1-add-a-simple-ai-chatbot)

## CHAT-3: Enhance AgentState for Provider Configuration

[Type: Story] - Enhance AgentState for Provider Configuration

### Summary
Modify `AgentState` to track which LLM provider was used during a run.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
3

#### Description
Add an attribute `provider_name` to `AgentState` and update serialization/deserialization accordingly. This allows downstream components to know which provider produced the response.

#### Problem and Solution
Problem: No trace of provider used; hard to debug or audit. 
Solution: Store provider name in state.

#### Impact Analysis
`src/agent/state.py`, any code that serializes `AgentState`.

#### Desired Path
1. Update dataclass definition.
2. Adjust any persistence logic.
3. Add tests verifying provider tracking.

#### Verification
Run unit tests ensuring state includes provider info.

#### Acceptance Criteria
- AC-1: `AgentState` contains `provider_name` field.
- AC-2: State serialization preserves the field.
- AC-3: Tests confirm correct value after a run.

#### Definition of Done (DoD)
- Code follows Black formatting.
- Code passes Ruff linting.
- Unit tests added/updated and passing.

## CHAT-4: End-to-End Integration Test (OpenAI & Ollama)

[Type: Story] - End-to-End Integration Test (OpenAI & Ollama)

### Summary
Create or update integration tests to verify real LLM responses and node transitions for both OpenAI and Ollama.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
5

#### Description
Write `tests/test_graph.py` that:
- Spins up the graph with OpenAI provider.
- Sends a sample query and asserts response structure.
Solution: Add comprehensive integration tests.

#### Impact Analysis
`tests/test_graph.py`, possibly `src/agent/graph.py` for test hooks.

#### Desired Path
1. Implement test harness.
2. Mock external calls if needed.
3. Ensure coverage >80%.

#### Verification
Run `pytest tests/test_graph.py` and confirm all assertions pass.

#### Acceptance Criteria
- AC-1: Tests cover both providers.
#### Definition of Done (DoD)
- Code follows Black formatting.
## CHAT-5: Documentation and ADR for AI Chatbot Implementation

[Type: Story] - Documentation and ADR for AI Chatbot Implementation

### Summary
Create an Architecture Decision Record documenting the model selection strategy and integration approach, and update documentation accordingly.

#### As-a / I-want / So-what
**As a** architect, **I want** to record decisions, **So that** future maintainers understand the rationale.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
3

#### Description
Write `docs/adr/ai_chatbot_integration.md` explaining:
- Choice of langchain providers.  
- Environment variable configuration.  
- Provider switching logic.  
- Testing strategy.

#### Problem and Solution
Problem: Lack of documented design decisions.  
Solution: Produce ADR and update README.

#### Impact Analysis
`docs/adr/`, `README.md`.

#### Desired Path
1. Draft ADR using template.
2. Review with team.
3. Commit to repo.

#### Verification
Ensure ADR file exists and is referenced in documentation.

#### Acceptance Criteria
- AC-1: ADR file created under `docs/adr`.
- AC-2: README updated to reference ADR.
- AC-3: PR passes all checks.

#### Definition of Done (DoD)
- Code follows Black formatting.
- Code passes Ruff linting.
- Unit tests added/updated and passing.

  ## Epic 2: Make the Application Docker Ready
**Goal:** Ensure the application is fully containerized, configurable via environment variables, and ready for CI/CD deployment.

### Tickets
| Ticket ID | Title | Description |
| :--- | :--- | :--- |
| **DOCK-1** | Refactor Dockerfile for Production Readiness | Optimize `docker/Dockerfile` using multi-stage builds and a non-root user for security. |
| **DOCK-2** | Configure Docker Compose for Multi-Service Setup | Update `docker/docker-compose.yml` to include an Ollama service container for local development/testing. |
| **DOCK-3** | Implement Environment Variable Management | Ensure all secrets (OpenAI keys, etc.) are handled via `.env` and passed correctly through Docker layers. |
| **DOCK-4** | Setup CI/CD Pipeline for Docker Registry Push | Create GitHub Actions workflows to build and push images to a container registry (e.g., GHCR). |
| **DOCK-5** | Documentation and ADR for Containerization Strategy | Finalize the PR and create an Er ADR in `docs/adr/` documenting the container orchestration and CI/CD flow. |

---

## Implementation Standards
- **Branching:** One branch per ticket.
- **Pull Requests:** One PR per ticket.
- **Validation:** Every PR must pass `make format`, `make check`, and `make test`.
- **Traceability:** Each completed Epic must conclude with an ADR in the `docs/adr/` directory.

## Verification Plan
1.  **Manual Testing:** Verify end-to-end chat functionality by sending requests to the `/chat` endpoint via `curl` while running the Docker Compose stack.
2.  **Automated Testing:** Ensure all new nodes and transitions maintain >80% test coverage in `tests/`.
3.  **CI/CD Validation:** Confirm that pushing code triggers the automated build and registry push process.
