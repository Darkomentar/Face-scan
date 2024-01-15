from sqlalchemy import desc, select
from app.database import gen_session


class BaseDAO:
    model=None

    @classmethod
    async def find_by_id(cls, model_id: int):
        async with gen_session() as session: 
            query = select(cls.model).filter_by(id=model_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_one_or_none(cls, **filter_by):
        async with gen_session() as session: 
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def find_all(cls, **filter_by):
        async with gen_session() as session: 
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_top_n(cls, limit: int, **filter_by):
        async with gen_session() as session:
            query = select(cls.model).filter_by(**filter_by).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()
        
    @classmethod
    async def find_last_n(cls, limit: int, **filter_by):
        async with gen_session() as session:
            # Предполагается, что у модели есть поле created_at для сортировки
            query = select(cls.model).filter_by(**filter_by).order_by(desc(cls.model.id)).limit(limit)
            result = await session.execute(query)
            return result.scalars().all()