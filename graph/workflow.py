from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.planner import planner_node

from agents.sql_agent import sql_agent
from agents.analytics_agent import analytics_agent
from agents.forecast_agent import forecast_agent

from agents.report_agent import report_agent
builder = StateGraph(AgentState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("sql", sql_agent)
builder.add_node("analytics", analytics_agent)
builder.add_node("forecast", forecast_agent)
builder.add_node("report", report_agent)

# Entry Point
builder.set_entry_point("planner")

# Planner routing
builder.add_conditional_edges(
    "planner",
    lambda state: state["agent"],
    {
        "sql": "sql",
    },
)

# Workflow
# Workflow
builder.add_edge("sql", "analytics")
builder.add_edge("analytics", "forecast")   # <-- Add this line
builder.add_edge("forecast", "report")
builder.add_edge("report", END)

graph = builder.compile()