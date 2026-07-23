def planner_node(state):
    query = state["query"].lower()

    if "customer" in query or "churn" in query:
        state["agent"] = "sql"

    elif "forecast" in query or "predict" in query:
        state["agent"] = "forecast"

    elif "report" in query:
        state["agent"] = "report"

    else:
        state["agent"] = "analytics"

    return state