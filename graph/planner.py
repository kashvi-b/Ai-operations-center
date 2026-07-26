def planner_node(state):
    query = state["query"].lower()

    if "forecast" in query or "predict" in query:
        state["intent"] = "forecast"

    elif "report" in query:
        state["intent"] = "report"

    else:
        state["intent"] = "analysis"

    return state