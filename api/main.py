from fastapi import FastAPI

app = FastAPI(
    title="Enterprise AI Operations Center",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Enterprise AI Operations Center Running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }