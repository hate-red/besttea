from sqlalchemy import select

from app.database import async_session_maker


class BaseRepository:
    model = None


    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by) # type: ignore
            result = await session.execute(query)
        
            return result.scalar_one_or_none()


    @classmethod
    async def filter(cls, **filter_by) -> list:
        async with async_session_maker() as session:
            query = select(model).filter_by(**filter_by) # type: ignore
            result = await session.execute(query)
        
            return result.scalars().all() # type: ignore


    @classmethod
    async def update(cls, instance) -> None:
        async with async_session_maker() as session:
            async with session.begin():
                session.add(instance)

                try:
                    await session.commit()
                except Exception as e:
                    await session.rollback()
                    raise e


    @classmethod
    async def delete(cls, instance) -> None:
        async with async_session_maker() as session:
            async with session.begin():
                await session.delete(instance)
                
                try:
                    await session.commit()
                except Exception as e:
                    await session.rollback()
                    raise e
