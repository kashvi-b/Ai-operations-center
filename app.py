from graph.workflow import graph

response = graph.invoke(
    {
        "query": "Show customers with highest churn probability",
        "agent": "",
        "result": [],
        "analytics": {}
    }
)

print("\n========== SQL Result ==========\n")
print(response["result"])

print("\n========== Analytics ==========\n")
print(response["analytics"])