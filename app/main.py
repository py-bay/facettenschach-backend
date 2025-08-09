# app/main.py
import os
import uuid
from fastapi import FastAPI, UploadFile, BackgroundTasks, Depends, HTTPException
from sqlmodel import SQLModel, Field, create_engine, Session, select
from typing import Optional
from pydantic import BaseModel

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./dev.db")
engine = create_engine(
    DATABASE_URL,
    connect_args=(
        {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
    ),
)

app = FastAPI(title="MVP")


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.get("/test")
async def test_endpoint():
    return {"message": "Hello, World!"}
