from app.models.posts.post_model import Genre, PostGenres, Post
from app.models.basemodel import db_connection, db
from app.queries.genres import create_genre, delete_genre, get_genres
from app.queries.posts import create_post, get_all_films, get_film_by_id
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router

from fastapi import FastAPI
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis.utils import from_url

@db
def create_tables() -> None:
    db_connection.create_tables([Genre, Post, PostGenres])

create_tables()

app = FastAPI()
app.include_router(router)


@app.on_event("startup")
async def startup():
    redis = from_url("redis://localhost", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")