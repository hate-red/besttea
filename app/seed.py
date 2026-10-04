import asyncio

from sqlalchemy import select, insert
from sqlalchemy.orm import Session

import pandas as pd

from app.database import async_session_maker
from app.models.films import Film, Genre, FilmGenres

from ml.config import (
    dataset_dir, 
    dataset_with_embeddings_name, 
)


async def seed(instances: list) -> list:
    async with async_session_maker() as session:
        async with session.begin():
            session.add_all(instances)

            try:
                await session.commit()
                return instances
            except Exception as e:
                await session.rollback()
                raise e


async def main() -> None:
    df = pd.read_pickle(dataset_dir / dataset_with_embeddings_name)

    genre_names = df['genres'].explode().unique().dropna().tolist()
    genres = [Genre(name=name) for name in genre_names]

    genre_instances = await seed(genres)
    genre_instances = {instance.name: instance for instance in genre_instances}

    films = []
    for row in df.to_dict(orient='records'):
        row['genres'] = [genre_instances[genre_name] for genre_name in row['genres']]
        films.append(Film(**row))

    await seed(films)


if __name__ == "__main__":
    asyncio.run(main())
