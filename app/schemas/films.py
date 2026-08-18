from pydantic import BaseModel

from datetime import date


class FilmResponse(BaseModel):
    tmdb_id:               int

    title:                 str
    genres:                list[str]
    overview:              str | None = None
    original_language:     str
    production_companies:  str
    tagline:               str | None = None

    release_date:          date | None = None

    vote_average:          float
    vote_count:            float
    popularity:            float
    budget:                float
    revenue:               float
    runtime:               float