from langgraph.graph import StateGraph, START, END

from graph.state import AgentState
from graph.planner import planner_node

from agents.sql_agent import sql_agent
from agents.analytics_agent import analytics_agent
from agents.forecast_agent import forecast_agent
from agents.report_agent import report_agent
from agents.visualization_agent import visualization_agent

builder = StateGraph(AgentState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("sql", sql_agent)
builder.add_node("analytics", analytics_agent)
builder.add_node("forecast", forecast_agent)
builder.add_node("report", report_agent)
builder.add_node("visualization", visualization_agent)

# Entry Point
builder.add_edge(START, "planner")

# Route based on intent
builder.add_conditional_edges(
    "planner",
    lambda state: state["intent"],
    {
        "analysis": "sql",
        "forecast": "sql",
        "report": "sql",
    },
)

# Workflow
builder.add_edge("sql", "analytics")
builder.add_edge("analytics", "visualization")
builder.add_edge("visualization", "forecast")
builder.add_edge("forecast", "report")
builder.add_edge("report", END)

graph = builder.compile()
