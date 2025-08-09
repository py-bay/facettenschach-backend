from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlmodel import Session
from app.schemas.category import CategoryCreate, CategoryRead, CategoryUpdate
import app.crud.category as crud
from app.api.v1.deps import get_db

router = APIRouter(prefix="/categories", tags=["categories"])

@router.post("/", response_model=CategoryRead, status_code=status.HTTP_201_CREATED)
def create_category(payload: CategoryCreate, db: Session = Depends(get_db)):
    category = crud.create_category(db, payload)
    return category

@router.get("/", response_model=List[CategoryRead])
def read_categories(limit: int = 100, offset: int = 0, db: Session = Depends(get_db)):
    return crud.get_categories(db, limit=limit, offset=offset)

@router.get("/{category_id}", response_model=CategoryRead)
def read_category(category_id: str, db: Session = Depends(get_db)):
    category = crud.get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.put("/{category_id}", response_model=CategoryRead)
def update_category(category_id: str, payload: CategoryUpdate, db: Session = Depends(get_db)):
    category = crud.update_category(db, category_id, payload)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category

@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(category_id: str, db: Session = Depends(get_db)):
    ok = crud.delete_category(db, category_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Category not found")
    return None
