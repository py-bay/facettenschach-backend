from sqlmodel import create_engine, SQLModel, Session
from .config import get_settings

settings = get_settings()
DATABASE_URL = settings.DATABASE_URL

# For Postgres use psycopg driver via connection string in .env
engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
