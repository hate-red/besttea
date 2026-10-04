from fastapi import FastAPI

from app.routers.films import router as films_router


app = FastAPI(title='BestTea API')


@app.get('/')
async def root() -> dict:
    return {'message': 'hi there!'}


app.include_router(films_router)
