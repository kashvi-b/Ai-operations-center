from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.planner import planner_node

from agents.sql_agent import sql_agent
from agents.analytics_agent import analytics_agent

builder = StateGraph(AgentState)

# Nodes
builder.add_node("planner", planner_node)
builder.add_node("sql", sql_agent)
builder.add_node("analytics", analytics_agent)

# Entry Point
builder.set_entry_point("planner")

# Planner decides which agent to execute
builder.add_conditional_edges(
    "planner",
    lambda state: state["agent"],
    {
        "sql": "sql",
    },
)

# SQL → Analytics
builder.add_edge("sql", "analytics")

# Analytics → End
builder.add_edge("analytics", END)

graph = builder.compile()