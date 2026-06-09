from typing import Literal
from langgraph.graph import StateGraph, END
from .state import AgentState

def chatbot(state: AgentState):
    # A simple chatbot node that just echoes the last message
    messages = state['messages']
    last_message = messages[-1]
    return {"messages": [f"Echo: {last_message.content}"]}

workflow = StateGraph(AgentState)

workflow.add_node("chatbot", chatbot)
workflow.set_entry_point("chatbot")
workflow.add_edge("chatbot", END)

app = workflow.compile()
