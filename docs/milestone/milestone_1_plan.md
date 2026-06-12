# Milestone 1: Jira Tickets Plan

This document outlines the breakdown of Epics into actionable Jira tickets for Milestone 1. Each ticket is designed to be implemented in a single branch and finalized with a single Pull Request (PR), followed by an Architecture Decision Record (ADR).

## Epic 1: Add a Simple AI Chatbot
**Goal:** Transition from mock nodes to real LLM integration (Ollama) and ensure end-to-end flow.

## CHAT-1: Implement Ollama Integration in Researcher Node

[Type: Story] - Implement Ollama Integration in Researcher Node

### Summary
Add support for a local Ollama LLM in the Researcher node using `langgraph_ollama`, configuring the local endpoint via environment variables.

#### As-a / I-want / So-what
**As a** developer, **I want** to replace mock responses with local Ollama model calls, **So that** we can test end‑to‑end without incurring API costs.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
5

#### Description
The current Researcher node uses mock responses. This ticket replaces the mock with local Ollama calls by integrating `langgraph_ollama`. The implementation will:
- Import and configure the Ollama LLM via langgraph.
- Read `OLLAMA_API_URL` (e.g. `http://localhost:11434`) from environment variables.
- Update the graph to use the Ollama provider and make provider selection rely on `LLM_PROVIDER` env var (default `ollama`).

#### Problem and Solution
Problem: No local LLM integration, limiting offline/no-cost testing.  
Solution: Replace mock with local Ollama calls via langgraph.

#### Impact Analysis
`src/agent/graph.py`, `src/agent/state.py` (provider tracking), `requirements.txt`.

#### Desired Path
1. Add `langgraph_ollama` to requirements.  
2. Update node implementation to call Ollama.  
3. Add env var `OLLAMA_API_URL` to docs and `.env` examples.  
4. Write unit tests mocking Ollama responses.

#### Verification
Run `pytest tests/test_graph.py` with the Ollama path and ensure the Researcher node returns model responses (mocked for CI).

#### Acceptance Criteria
 - AC-1: The Researcher node uses `langgraph_ollama` when `LLM_PROVIDER=ollama`.  
- AC-2: Endpoint is read from `OLLAMA_API_URL` env var.  
- AC-3: Unit tests pass with mocked Ollama responses.

#### Definition of Done (DoD)
- Code follows Black formatting.  
- Code passes Ruff linting.  
- Unit tests added/updated and passing.  
- ADR updated to document Ollama choice.

#### Reference
[Epic 1](docs/milestone/milestone_1_plan.md#epic-1-add-a-simple-ai-chatbot)

## CHAT-2: Implement Ollama Integration in Writer Node

[Type: Story] - Implement Ollama Integration in Writer Node

### Summary
Add support for local LLM via Ollama in the Writer node, enabling provider switching.

#### As-a / I-want / So-what
**As a** developer, **I want** to use a local LLM for faster iteration, **So that** we can test without external API calls.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
5

#### Description
Update the Writer node to call an Ollama endpoint using `langgraph_ollama`. The graph should be configurable to use either OpenAI or Ollama based on environment variables.

#### Problem and Solution
Problem: Only OpenAI is supported, limiting local testing. 
Solution: Integrate Ollama provider via langgraph.

#### Impact Analysis
`src/agent/graph.py`, `src/agent/state.py` (provider config).

#### Desired Path
1. Add `langgraph_ollama` to requirements.
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

#### As-a / I-want / So-what
**As a** developer, **I want** state to record the provider name, **So that** we can audit and debug runs.

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

#### As-a / I-want / So-what
**As a** QA engineer, **I want** automated end‑to‑end tests, **So that** we can ensure reliability across providers.

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
- Code passes Ruff linting.
## CHAT-5: Documentation and ADR for AI Chatbot Implementation

[Type: Story] - Documentation and ADR for AI Chatbot Implementation

### Summary
Create an Architecture Decision Record documenting the model selection strategy and integration approach, and update documentation accordingly.

#### As-a / I-want / So-what
**As a** architect, **I want** to record decisions, **So that** future maintainers understand the rationale.

#### As-a / I-want / So-what
**As a** architect, **I want** to record decisions, **So that** future maintainers understand the rationale.

#### Parent Epic
Epic 1: Add a Simple AI Chatbot

#### Story Points
3

#### Description
- Write `docs/adr/ai_chatbot_integration.md` explaining:
- Choice of langgraph providers.  
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
