# Project Context for AI Agents

This repository contains a template for building multi-agent AI chatbots using LangGraph, designed for deployment in Docker containers.

## Architecture
The system uses a graph-based orchestration approach with LangGraph. Agents are nodes in the graph, and edges define the flow of control between them.

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
