from typing import TypedDict

class AgentState(TypedDict):
    query: str
    agent: str
    result: str