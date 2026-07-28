from fastapi import FastAPI
from pydantic import BaseModel

from graph.workflow import graph

app = FastAPI(
    title="Enterprise AI Operations Center API"
)


class Query(BaseModel):
    query: str


@app.post("/analyze")
def analyze(request: Query):

    response = graph.invoke(
        {
            "query": request.query,
            "intent": "",
            "result": [],
            "analytics": {},
            "charts": {},
            "forecast": {},
            "report": ""
        }
    )

    return {
        "result": response["result"],
        "analytics": response["analytics"],
        "forecast": response["forecast"],
        "report": response["report"]
    }