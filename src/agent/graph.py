from typing import Literal
from langgraph.graph import StateGraph, END
from .state import AgentState

# Define agent nodes

def researcher(state: AgentState):
    messages = state['messages']
    last_message = messages[-1]
    return {"messages": [f"Researcher found info about: {last_message.content}"]}

def writer(state: AgentState):
    messages = state['messages']
    last_message = messages[-1]
    return {"messages": [f"Writer summarized: {last_message.content}"]}

# Build graph
workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)
workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)
app = workflow.compile()
