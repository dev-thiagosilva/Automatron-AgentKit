# Milestone 1: Jira Tickets Plan

This document outlines the breakdown of Epics into actionable Jira tickets for Milestone 1. Each ticket is designed to be implemented in a single branch and finalized with a single Pull Request (PR), followed by an Architecture Decision Record (ADR).

## Epic 1: Add a Simple AI Chatbot
**Goal:** Transition from mock nodes to real LLM integration (OpenAI & Ollama) and ensure end-to-end flow.

### Tickets
| Ticket ID | Title | Description |
| :--- | :--- | :--- |
| **CHAT-1** | Implement OpenAI Integration in Researcher Node | Update `src/agent/graph.py` to use `langchain_openai`. Configure environment variables for API keys. |
| **CHAT-2** | Implement Ollama Integration in Writer Node | Update nodes to support local LLM via Ollama. Ensure the graph can switch between providers based on configuration. |
| **CHAT-3** | Enhance AgentState for Provider Configuration | Modify `src/agent/state.py` if necessary to track which model/provider was used during the run. |
| **CHAT-4** | End-to-End Integration Test (OpenAI & Ollama) | Create/Update `tests/test_graph.py` to verify real LLM responses and node transitions. |
| **CHAT-5** | Documentation and ADR for AI Chatbot Implementation | Finalize the PR and create an ADR in `docs/adr/` documenting the model selection and integration strategy. |

---

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
