from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
from langgraph.graph.message import add_messages
from src.agent.state import AgentState
from src.agent.graph import app as graph_app

class Message(BaseModel):
    content: str

app = FastAPI()

@app.post("/chat")
async def chat(messages: List[Message]):
    from langchain_core.messages import HumanMessage, AIMessage
    state_messages = [HumanMessage(content=m.content) for m in messages]
    initial_state = {"messages": state_messages}
    output_state = graph_app.invoke(initial_state)
    return {"response": output_state["messages"][-1].content}
