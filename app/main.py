from fastapi import FastAPI

app = FastAPI(title="pulsar-api")


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}


@app.get("/")
def root() -> dict:
    return {"service": "pulsar-api", "message": "Launched with Launchbay"}
