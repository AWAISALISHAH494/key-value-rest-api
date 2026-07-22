from fastapi import FastAPI
from .database import engine, Base
from .routers.kv_router import router as kv_router

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Key-Value REST API ",
    description="A simple Key-Value store built with FastAPI + PostgreSQL",
    version="1.0.0"
)

app.include_router(kv_router)

@app.get("/health")
def health_check():
    return {"status": "healthy", "message": "Key-Value API is running"}