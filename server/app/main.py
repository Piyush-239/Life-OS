from fastapi import FastAPI

from app.api.routes import health

app = FastAPI(
    title="LIFE-OS",
    version="0.1.0",
    description="A lifelong AI operating system."
)

app.include_router(health.router)


@app.get("/")
def root():
    return {
        "project": "LIFE-OS",
        "status": "running",
        "version": "0.1.0",
        "message": "Hello, Piyush. LIFE-OS is online."
    }