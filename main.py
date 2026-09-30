from contextlib import asynccontextmanager
from fastapi import FastAPI
from database import create_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    print("Database tables created")
    yield
    #shutdown: cleanup here
    print("Shutting down the app")

app = FastAPI(
    title="Rangmanch Review API",
    description="Theater review API built with FastAPI and SQLModel",
    lifespan=lifespan
)

@app.get("/")
def root():
    return {"message": "Welcome to the Rangmanch Review API!"}



