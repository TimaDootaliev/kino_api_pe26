from app.queries.posts import (
    get_all_films, 
    get_film_by_id, 
    create_post
    )
from app.schemas.posts import PostCreateSchema

from fastapi_cache.decorator import cache


from fastapi import APIRouter

router = APIRouter()

@router.get('/posts')
@cache(20)
def get_films():
    return get_all_films()


@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)


# TODO: дописать пути для остальных функций