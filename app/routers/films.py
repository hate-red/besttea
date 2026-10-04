from fastapi import APIRouter


router = APIRouter(prefix='/films', tags=['films'])


@router.get('/{id}')
async def get_film(id: int) -> dict:
    return {'id': id}
