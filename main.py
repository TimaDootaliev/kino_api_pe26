from datetime import date
from fastapi import FastAPI

from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router

@db
def create_tables() -> None:
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()


# app = FastAPI()
# app.include_router(router, prefix='/posts')

print(get_film_by_id(1))