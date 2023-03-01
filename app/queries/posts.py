from app.models.posts.post_model import Post, PostGenres, Genre
from app.models.basemodel import db
from peewee import fn
from datetime import date
from typing import List
# TODO: написать CRUD для модели Posts

@db
def create_post(
        title: str, 
        description: str, 
        year: date, 
        country: str, 
        genres: List):
    post = Post.create(
        title=title, description=description, 
        year=year, country=country
        )
    for genre in genres:
        g = Genre.get(title=genre)
        post.genre.add(g)
    return post


@db
def get_film_with_genres(post_id):
    query = (Post
         .select(Post, fn.array_agg(Genre.title).alias('genre_titles'))
         .join(PostGenres)
         .join(Genre)
         .where(Post.id == post_id)
         .group_by(Post.id).get())
    return query