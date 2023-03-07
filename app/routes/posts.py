from fastapi import APIRouter

from app.queries.posts import get_all_films, get_film_by_id, create_post

router = APIRouter()


@router.get('/')
def get_films():
    return get_all_films()


@router.get('/{id}')
def get_one_film(id: int):
    return get_film_by_id(id)
