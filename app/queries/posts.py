from app.models.posts.post_model import Post, PostGenres, Genre
from app.schemas.posts import PostAllSchema, PostOneSchema, PostCreateSchema
from app.models.basemodel import db
from datetime import date
from typing import List
from peewee import fn


@db
def create_post(post_in: PostCreateSchema):
    post = Post.create(
        title=post_in.title,
        description=post_in.description,
        year=post_in.year,
        country=post_in.country
    )
    for genre in post_in.genre:
        g = Genre.get(title=genre)
        post.genre.add(g)
    return post

@db
def get_all_films() -> list[PostAllSchema]:
    posts = Post.select(Post.id, Post.title, Post.year)
    return [PostAllSchema.from_orm(post) for post in posts]


@db
def get_film_by_id(id) -> Post:
    post = Post.select(Post, fn.array_agg(Genre.title).alias('genre_titles')).join(PostGenres).join(Genre).where(Post.id == id).group_by(Post.id).get_or_none()
    if post:
        return PostOneSchema.from_orm(post)
    return None

    
# TODO: дописать CRUD для модели Posts
# TODO: ознакомиться с документацией https://fastapi.tiangolo.com/ 
# TODO: ознакомиться с документацией https://docs.pydantic.dev/

