# Project Context for AI Agents

This repository provides a **template** for building low‑latency multi‑agent chatbots that can be deployed in Docker containers. It is built around **LangGraph**, a lightweight orchestration framework that lets you compose agents as nodes in a directed graph.

## Architecture Overview

```
User → FastAPI /chat endpoint → LangGraph workflow (Researcher → Writer) → Response
```

* **FastAPI** exposes the chatbot via a simple REST API. The `/chat` endpoint accepts a list of messages and forwards them to the LangGraph graph.
* The **LangGraph** graph is defined in `src/agent/graph.py`. It currently contains two nodes:
  * **Researcher** – enriches or retrieves information based on the last user message.
  * **Writer** – formats the enriched data into a final response.

## Project Structure

```
src/
├─ agent/          # Core LangGraph logic (state, graph, orchestrator)
│   ├─ state.py
│   ├─ graph.py
│   └─ orchestrator.py
├─ agent_api/      # FastAPI wrapper
│   └─ api.py
└─ main.py         # Entrypoint for the container

tests/
├─ test_api.py
├─ test_graph.py

docker/
├─ Dockerfile
└─ docker-compose.yml

docs/
├─ context/project_overview.md   # This file
└─ diagram/project_structure.md  # Mermaid diagram of the repo layout
```

## Development Workflow

1. **Environment** – Create a virtual environment and install dependencies:
	```bash
	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt
	```
2. **Add Agents** – Implement new agent functions in `src/agent/` and register them with the graph.
3. **Test** – Run unit tests:
	```bash
	make test
	```
4. **Lint & Format** – Use Ruff for linting and Black for formatting:
	```bash
	make check
	make format
	```
5. **Containerize** – Build and run the container:
	```bash
	docker compose up --build
	```

## CI/CD

The repository includes a GitHub Actions workflow (`.github/workflows/test.yml`) that runs tests, lints with Ruff, and ensures an 80 % test‑coverage threshold.

Feel free to extend the graph or add new API endpoints as needed – this template is intentionally lightweight so you can iterate quickly.

## Core Components
- `src/state.py`: Defines the shared state (AgentState) used across all agents.
- `src/graph.py`: Defines the LangGraph workflow, including nodes (agents) and edges.
- `tests/`: Contains unit tests for verifying agent logic and graph transitions.

## Development Workflow
1.  **Environment Setup**: Create a virtual environment and install dependencies from `requirements.txt`.
2.  **Adding Agents**: Define new agent functions in `src/` and add them as nodes to the `StateGraph` in `src/graph.py`.
3.  **Testing**: Run `pytest` to ensure changes don't break existing functionality.
4.  **Containerization**: Use `docker-compose up --build` to run the chatbot in a containerized environment.

## Deployment
The project is Docker-ready. The `Dockerfile` in `docker/` handles the build process, and `docker-compose.yml` manages the runtime configuration.
