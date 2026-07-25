from statistics import mean

def forecast_agent(state):
    data = state["result"]

    if not isinstance(data, list) or len(data) == 0:
        state["forecast"] = {
            "message": "No data available for forecasting."
        }
        return state

    revenues = [row["monthly_revenue"] for row in data]

    avg_revenue = mean(revenues)

    predicted_next_month = round(avg_revenue * 1.05, 2)  # Assume 5% growth

    state["forecast"] = {
        "current_average_revenue": round(avg_revenue, 2),
        "predicted_next_month_revenue": predicted_next_month,
        "growth_assumption": "5%"
    }

    return state