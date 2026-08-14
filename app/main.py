from fastapi import FastAPI


app = FastAPI(title='BestTea API')


@app.get('/')
async def root() -> dict:
    return {'message': 'hi there!'}
