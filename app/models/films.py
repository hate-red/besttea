from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import ARRAY

from datetime import date

from app.database import Base


class Film(Base):
    __tablename__ = 'films'

    id:                    Mapped[int] = mapped_column(primary_key=True)
    tmdb_id:               Mapped[int]

    title:                 Mapped[str]
    genres:                Mapped[list[str]] = mapped_column(ARRAY(String))
    overview:              Mapped[str] = mapped_column(nullable=True)
    original_language:     Mapped[str]
    production_companies:  Mapped[str]
    tagline:               Mapped[str] = mapped_column(nullable=True)

    release_date:          Mapped[date] = mapped_column(nullable=True)

    vote_average:          Mapped[float]
    vote_count:            Mapped[float]
    popularity:            Mapped[float]
    budget:                Mapped[float]
    revenue:               Mapped[float]
    runtime:               Mapped[float]


    def __str__(self) -> str:
        return f'Title: {self.title} | Vote avg: {self.vote_average}'
