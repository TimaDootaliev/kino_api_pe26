from pydantic import BaseModel
from datetime import date
from typing import List, Any

from app.models.posts.post_model import Genre, Post


class GenreIn(BaseModel):
    title: str

class GenreOut(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class PostShow(BaseModel):
    title: str
    description: str
    year: date
    country: str
    genre: Any

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class PostCreate(BaseModel):
    id: int
    title: str
    description: str
    year: date
    country: str
    genres: List[GenreOut]

    class Config:
        orm_mode = True

