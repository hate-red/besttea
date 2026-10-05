from app.repositories.base import BaseRepository
from app.models.films import Film


class FilmRepository(BaseRepository):
    model = Film
