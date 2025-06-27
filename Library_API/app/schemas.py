from pydantic import BaseModel
from typing import Optional
from datetime import date

class BookBase(BaseModel):
    title: str
    author: str
    genre: Optional[str] = None
    status: str  # 'read', 'reading', 'want to read'
    rating: Optional[int] = None
    review: Optional[str] = None
    completion_date: Optional[date] = None

class BookCreate(BookBase):
    pass

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
