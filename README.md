# Low‑Latency Multi‑Agent Chatbot

This repository is a production‑grade template for building **low‑latency** multi‑agent chatbots. It leverages:

- **LangGraph** – to orchestrate agents in a directed graph.
- **FastAPI** – exposing a `/chat` REST endpoint that accepts a list of messages and triggers the workflow.
- **Docker** – fully containerized, ready for CI/CD pipelines.

## Features
- Extensible agent architecture: add new nodes (e.g., Fact‑Checker, Summarizer) with minimal boilerplate.
- End‑to‑end integration tests ensuring >80 % coverage.
- Secure by design – input sanitisation and prompt injection mitigation.
- Docker‑compose setup that includes an Ollama service for local LLM testing.

## Quick Start
```bash
# Build the container image
docker compose build

# Run the stack (FastAPI + Ollama)
docker compose up -d

# Send a chat request
curl -X POST http://localhost:8000/chat \
	-H "Content-Type: application/json" \
	-d '{"messages": [{"role": "user", "content": "Hello"}]}'
```

## Development
```bash
make format   # Run Black formatting
make check    # Run Ruff linting
make test     # Run Pytest unit tests
```

For more details, see the [docs](./docs/AI_Context/project_overview.md).
