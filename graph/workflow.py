from langgraph.graph import StateGraph, END

from graph.state import AgentState
from graph.planner import planner_node

from agents.sql_agent import sql_agent

builder = StateGraph(AgentState)

builder.add_node("planner", planner_node)
builder.add_node("sql", sql_agent)

builder.set_entry_point("planner")
builder.add_conditional_edges(
    "planner",
    lambda state: state["agent"],
    {
        "sql": "sql",
    },
)

builder.add_edge("sql", END)

graph = builder.compile()