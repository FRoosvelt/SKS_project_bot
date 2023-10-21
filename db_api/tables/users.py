from sqlalchemy import Column, Integer, BigInteger, Boolean

from db_api.database import Base


class Users(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    is_blocked = Column(Boolean, default=False)