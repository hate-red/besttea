from pydantic import BaseModel


class GenreResponse(BaseModel):
    id:                    int
    name:                  str


class FilmResponse(BaseModel):
    id:                    int

    title:                 str
    original_title:        str
    overview:              str
    original_language:     str

    genres:                list[GenreResponse]

    popularity:            float
    vote_average:          float
    vote_count:            float

    release_year:          int
    embedding:             list[float]
