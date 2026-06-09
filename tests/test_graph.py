import pytest
from langchain_core.messages import HumanMessage
from src.graph import app

def test_chatbot_echo():
    input_message = HumanMessage(content="Hello")
    initial_state = {"messages": [input_message]}
    output_state = app.invoke(initial_state)
    
    assert len(output_state["messages"]) == 2
    assert output_state["messages"][1].content == "Echo: Hello"
