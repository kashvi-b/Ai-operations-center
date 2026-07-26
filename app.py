from graph.workflow import graph

response = graph.invoke(
    {
    "query": "Generate business report",
    "intent": "",
    "result": [],
    "analytics": {},
    "charts": {},
    "forecast": {},
    "report": ""
    }
)

print("\n========== SQL Result ==========\n")
print(response["result"])

print("\n========== Analytics ==========\n")
print(response["analytics"])

print("\n========== Forecast ==========\n")
print(response["forecast"])

print("\n========== REPORT ==========\n")
print(response["report"])

# Show Plotly chart
charts = response["charts"]

if "revenue_chart" in charts:
    charts["revenue_chart"].show()