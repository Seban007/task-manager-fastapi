# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import models
from database import engine, Base
from routers import tasks, users

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="Task Manager with JWT")

# CORS configuration to allow React frontend
origins = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000",  # optional
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(tasks.router)

# Root endpoint
@app.get("/")
def root():
    return {"message": "Task Manager API (JWT) running"}
