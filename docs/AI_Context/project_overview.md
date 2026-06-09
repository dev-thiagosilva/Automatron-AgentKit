# Repository Context: Low-Latency LangGraph Agent API

<background_information>
This repository is a production-grade template for building low-latency multi-agent chatbots.

**Core Stack & Architecture:**
* **Orchestration:** LangGraph manages the directed graph of agents. The graph topology is defined in `src/agent/graph.py`, and the shared data structure is in `src/agent/state.py` (`AgentState`).
* **API Layer:** FastAPI (`src/agent_api/api.py`) exposes a `/chat` REST endpoint that accepts message lists and triggers the LangGraph workflow.
* **Current Workflow:** User → FastAPI → Researcher Node (Enrichment) → Writer Node (Formatting) → Response.
* **Infrastructure:** The application is strictly containerized using Docker (`docker/Dockerfile`, `docker-compose.yml`).
</background_information>

<instructions>
When exploring this repository or generating code, adhere strictly to the following heuristics:

1.  **Agent Addition Protocol:** When instructed to create a new agent:
    * Implement the node logic inside the `src/agent/` directory.
    * Evaluate if `src/agent/state.py` requires new fields to support the agent's output.
    * Register the new node and define its routing edges in `src/agent/graph.py`.
2.  **Quality & CI Standards:** The repository enforces an 80% test-coverage threshold via GitHub Actions. You must write corresponding unit tests in the `tests/` directory for any new agent or graph transition.
3.  **Local Tooling:** Before finalizing any code generation, format and lint your output as if running:
    * `make format` (Black)
    * `make check` (Ruff)
    * `make test` (Pytest)
4.  **Security & Observability:** Treat this as a high-security environment. Ensure all new nodes handle user inputs defensively to mitigate prompt injections. Where appropriate, structure outputs to support tracing and automated LLM-as-a-judge pipeline evaluations.
5.  **State Management:** If undertaking complex, multi-step refactoring, log your checklist and architectural updates in `docs/context/STATE.md` to prevent context degradation.
</instructions>

<canonical_examples>
**Task:** "Add a Fact-Checker agent after the Writer node."

**Expected Approach:**
1.  **State Check:** Review `src/agent/state.py` to ensure `AgentState` can hold a boolean validation flag or correction notes.
2.  **Implementation:** Create `src/agent/fact_checker.py` containing the node logic.
3.  **Graph Update:** Modify `src/agent/graph.py` by importing the fact-checker, adding it to the `StateGraph`, and updating the edges (e.g., routing `Writer` to `Fact-Checker`, and `Fact-Checker` to either `END` or back to `Writer`).
4.  **Testing:** Draft `tests/test_fact_checker.py` and update `tests/test_graph.py` to ensure the new routing logic maintains >80% coverage.
5.  **Validation:** Ensure code adheres to Ruff/Black formatting standards.
</canonical_examples>