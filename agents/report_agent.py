def report_agent(state):
    analytics = state.get("analytics", {})
    forecast = state.get("forecast", {})

    if not analytics or not forecast:
        state["report"] = "No report available."
        return state

    report = f"""
Enterprise AI Operations Report
================================

Total High-Risk Customers : {analytics['total_customers']}

Average Revenue           : ₹{analytics['average_revenue']:.2f}

Average Churn Probability : {analytics['average_churn_probability']}

Highest Churn Probability : {analytics['highest_churn_probability']}

Predicted Next Month Revenue : ₹{forecast['predicted_next_month_revenue']:.2f}

Growth Assumption : {forecast['growth_assumption']}
"""

    state["report"] = report

    return state