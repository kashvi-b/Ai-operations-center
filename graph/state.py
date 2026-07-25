from typing import TypedDict

class AgentState(TypedDict):
    query: str
    agent: str
    result: list | str
    analytics: dict
    forecast: dict
    report: str