from fastapi import APIRouter

from app.schemas.films import FilmResponse
from app.repositories.films import FilmRepository


router = APIRouter(prefix='/films', tags=['films'])


@router.get('/{id}')
async def get_film(id: int):
    film = await FilmRepository.get_one_or_none(id=id)
    
    return film
