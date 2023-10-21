from sqlite3 import IntegrityError

from sqlalchemy import select, func

from db_api.database import get_session
from db_api.tables.application import application_table


async def add_application(
        user_id: int,
        type: str,
        text: str
):
    async with get_session() as session:
        application = application_table(
            user_id=user_id,
            type=type,
            text=text
        )
        session.add(application)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()


async def select_application_id(user_id: int):
    async with get_session() as session:
        sql = select(func.count(application_table.id)).where(
            application_table.user_id == user_id
        )
        result = await session.execute(sql)
        return result.scalars()

async def select_cont_id_application():
    async with get_session() as session:
        sql = select(func.count(application_table.id))
        result = await session.execute(sql)
        return result.scalar()