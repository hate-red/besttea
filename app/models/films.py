from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from pgvector.sqlalchemy import Vector

from app.database import Base
from app.config import EMBEDDING_LENGTH


class Genre(Base):
    __tablename__ = 'genres'

    id:                    Mapped[int] = mapped_column(primary_key=True)
    name:                  Mapped[str]


    def __str__(self) -> str:
        return f'Name: {self.name}'


class Film(Base):
    __tablename__ = 'films'

    id:                    Mapped[int] = mapped_column(primary_key=True)

    title:                 Mapped[str]
    original_title:        Mapped[str]
    overview:              Mapped[str]
    original_language:     Mapped[str]

    genres:                Mapped[list['Genre']] = relationship(
                                secondary='film_genres',
                            )

    popularity:            Mapped[float]
    vote_average:          Mapped[float]
    vote_count:            Mapped[float]

    release_year:          Mapped[int]

    embedding:             Mapped[list[float]] = mapped_column(Vector(EMBEDDING_LENGTH))


    def __str__(self) -> str:
        return f'Title: {self.title} | Vote avg: {self.vote_average}'


class FilmGenres(Base):
    __tablename__ = 'film_genres'

    film_id:               Mapped[int] = mapped_column(ForeignKey('films.id'), primary_key=True)
    genre_id:              Mapped[int] = mapped_column(ForeignKey('genres.id'), primary_key=True)


    def __str__(self) -> str:
        return f'Film ID: {self.film_id} | Genre ID: {self.genre_id}'
