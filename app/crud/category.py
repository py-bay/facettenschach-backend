from sqlmodel import select, Session
from typing import List, Optional
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryUpdate

def get_category(session: Session, category_id: str) -> Optional[Category]:
    return session.get(Category, category_id)

def get_categories(session: Session, limit: int = 100, offset: int = 0) -> List[Category]:
    statement = select(Category).limit(limit).offset(offset)
    return session.exec(statement).all()

def create_category(session: Session, c: CategoryCreate) -> Category:
    category = Category.from_orm(c)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def update_category(session: Session, category_id: str, c: CategoryUpdate) -> Optional[Category]:
    category = session.get(Category, category_id)
    if not category:
        return None
    cat_data = c.dict(exclude_unset=True)
    for key, value in cat_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def delete_category(session: Session, category_id: str) -> bool:
    category = session.get(Category, category_id)
    if not category:
        return False
    session.delete(category)
    session.commit()
    return True
