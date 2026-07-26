import plotly.express as px


def visualization_agent(state):
    """
    Creates charts from SQL results.
    """

    data = state["result"]

    if not data or isinstance(data, str):
        state["charts"] = {}
        return state

    fig = px.bar(
        data,
        x="name",
        y="monthly_revenue",
        title="Top High-Risk Customers by Revenue",
    )

    state["charts"] = {
        "revenue_chart": fig
    }

    return state