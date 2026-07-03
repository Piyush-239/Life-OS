from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from app.api.routes import chat, health
from app.database.base import Base
from app.database.session import engine


app = FastAPI(
    title="LIFE-OS",
    version="0.1.0",
    description="A lifelong AI operating system.",
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Serve static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# API routes
app.include_router(health.router)
app.include_router(chat.router)


@app.get("/")
def home():
    return FileResponse("app/static/index.html")


@app.get("/status")
def status():
    return {
        "project": "LIFE-OS",
        "status": "running",
        "version": "0.1.0",
        "message": "Hello, Piyush. LIFE-OS is online.",
    }