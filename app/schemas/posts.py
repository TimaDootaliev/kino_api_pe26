from pydantic import BaseModel
from datetime import date
from typing import List, Any, Optional

from app.models.posts.post_model import Genre

class GenreSchema(BaseModel):
    title: str | None = None
    class Config:
        orm_mode = True


class PostAllSchema(BaseModel):
    id: int
    title: str
    year: date

    class Config:
        orm_mode = True

class PostOneSchema(BaseModel):
    id: int
    title: str
    description: str
    year: date
    country: str
    genre: GenreSchema

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class PostCreateSchema(BaseModel):
    title: str
    description: Optional[str]
    year: date
    country: str
    genre: List[str]

    class Config:
        orm_mode = True