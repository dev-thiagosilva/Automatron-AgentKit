from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    # The messages list will be updated by adding new messages to the existing ones
    messages: Annotated[list, add_messages]
