from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from src.agent.graph import app as graph_app

class Message(BaseModel):
    content: str

app = FastAPI()

@app.post("/chat")
async def chat(messages: List[Message]):
    from langchain_core.messages import HumanMessage
    state_messages = [HumanMessage(content=m.content) for m in messages]
    initial_state = {"messages": state_messages}
    output_state = graph_app.invoke(initial_state)
    return {"response": output_state["messages"][-1].content}
