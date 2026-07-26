from typing import TypedDict


class AgentState(TypedDict):
    # User input
    query: str

    # Intent identified by Planner Agent
    intent: str

    # SQL Agent output
    result: list

    # Analytics Agent output
    analytics: dict

    # Visualization Agent output
    charts: dict

    # Forecast Agent output
    forecast: dict

    # Report Agent output
    report: str