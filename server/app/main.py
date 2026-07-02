from fastapi import FastAPI
from app.api.routes import chat
from app.core.settings import get_settings
from app.api.routes import health



app = FastAPI(
    title="LIFE-OS",
    version="0.1.0",
    description="A lifelong AI operating system."
)

app.include_router(health.router)
app.include_router(chat.router)

from app.database.base import Base
from app.database.session import engine

Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {
        "project": "LIFE-OS",
        "status": "running",
        "version": "0.1.0",
        "message": "Hello, Piyush. LIFE-OS is online."
    }