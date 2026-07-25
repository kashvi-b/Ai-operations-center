from graph.workflow import graph

response = graph.invoke(
    {
        "query": "Show customers with highest churn probability",
        "agent": "",
        "result": [],
        "analytics": {},
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