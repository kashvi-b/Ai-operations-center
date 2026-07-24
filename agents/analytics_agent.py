def analytics_agent(state):
    """
    Analyze SQL query results and generate business metrics.
    """

    data = state["result"]

    # If SQL Agent returned an error
    if isinstance(data, str):
        return state

    if len(data) == 0:
        state["analytics"] = {
            "message": "No records found."
        }
        return state

    total_customers = len(data)

    avg_revenue = sum(
        customer.get("monthly_revenue", 0)
        for customer in data
    ) / total_customers

    avg_churn = sum(
        customer.get("churn_probability", 0)
        for customer in data
    ) / total_customers

    highest_churn = max(
        customer.get("churn_probability", 0)
        for customer in data
    )

    state["analytics"] = {
        "total_customers": total_customers,
        "average_revenue": round(avg_revenue, 2),
        "average_churn_probability": round(avg_churn, 2),
        "highest_churn_probability": highest_churn,
    }

    return state