from sqlalchemy import select, update
from sqlalchemy.exc import IntegrityError

from db_api.database import get_session
from db_api.tables.users import Users


async def add_user(
        user_id: int
):
    async with get_session() as session:
        user = Users(
            user_id=user_id
        )
        session.add(user)
        try:
            await session.commit()
        except IntegrityError:
            await session.rollback()

async def select_all_users():
    async with get_session() as session:
        sql = select(Users.user_id)
        result = await session.execute(sql)
        return result.scalars()


async def select_user_id(user_id: int):
    async with get_session() as session:
        sql = select(Users).where(
            Users.user_id == user_id
        )
        result = await session.execute(sql)
        return result.scalar()

async def update_user_ban_status(user_id: int, ban_status: bool):
    async with get_session() as session:
        sql = update(Users).where(
            Users.user_id == user_id
        ).values(is_blocked=ban_status)
        await session.execute(sql)
        await session.commit()