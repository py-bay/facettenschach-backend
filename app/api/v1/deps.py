from typing import Generator
from app.core.database import get_session

def get_db():
    yield from get_session()
