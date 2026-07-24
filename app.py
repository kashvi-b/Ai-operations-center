from graph.workflow import graph

response = graph.invoke(
    {
        "query": "Show customers with highest churn probability",
        "agent": "",
        "result": [],
        "analytics": {}
    }
)

print(response)