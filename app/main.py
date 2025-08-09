from fastapi import FastAPI
from app.core.config import get_settings
from app.core.database import create_db_and_tables
from app.api.v1 import category as category_router

def create_app() -> FastAPI:
    app = FastAPI(title="Facettenschach - Categories API")
    app.include_router(category_router.router)
    return app

app = create_app()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
