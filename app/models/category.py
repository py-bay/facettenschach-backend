from typing import Optional
from sqlmodel import SQLModel, Field
import uuid

def gen_uuid() -> str:
    return str(uuid.uuid4())

class Category(SQLModel, table=True):
    id: str = Field(default_factory=gen_uuid, primary_key=True, index=True)
    name: str
