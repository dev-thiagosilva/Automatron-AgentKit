from typing import Literal
from langgraph.graph import StateGraph, END
from .state import AgentState

def researcher(state: AgentState):
    # A simple researcher node that adds information to the message
    messages = state['messages']
    last_message = messages[-1]
    return {"messages": [f"Researcher found info about: {last_message.content}"]}

def writer(state: AgentState):
    # A simple writer node that summarizes the research
    messages = state['messages']
    last_message = messages[-1]
    return {"messages": [f"Writer summarized: {last_message.content}"]}

def router(state: AgentState) -> Literal["researcher", "writer"]:
    # A simple router that decides where to go next
    messages = state['messages']
    if "research" in messages[-1].content.lower():
        return "researcher"
    return "writer"

workflow = StateGraph(AgentState)

workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)

workflow.set_entry_point("router")
workflow.add_conditional_edges("router", router, {"researcher": "researcher", "writer": "writer"})
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

# Note: Since 'router' is a function used in conditional edges, 
# we need to add it as a node if we want to use it as an entry point or just use it directly.
# In LangGraph, you can set an entry point to a node. Let's make router a node.

workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)
workflow.add_node("router_node", lambda state: state) # Dummy node for routing logic if needed, but conditional edges are better

# Let's simplify: entry point is a node that then uses conditional edges.
workflow = StateGraph(AgentState)
workflow.add_node("researcher", researcher)
workflow.add_node("writer", writer)

workflow.set_entry_point("researcher")
workflow.add_edge("researcher", "writer")
workflow.add_edge("writer", END)

# Actually, let's stick to a simple multi-agent: Researcher -> Writer -> End
# with a conditional edge from the start if we want.

app = workflow.compile()
