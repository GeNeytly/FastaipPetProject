from sqlalchemy import select, insert

from app.database import async_session_maker


class BaseDAO:
    model = None

    @classmethod
    async def get_all(cls):
        async with async_session_maker() as session:
            query = select(cls.model)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]
            return result

    @classmethod
    async def add(cls, **data) -> None:
        async with async_session_maker() as session:
            query = insert(cls.model).values(**data)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def get_one_or_none(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            # result = [row[0].to_read_model() for row in result.all()]
            #
            return result.scalar_one_or_none()

    @classmethod
    async def get_filtered(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            result = [row[0].to_read_model() for row in result.all()]
            return result
