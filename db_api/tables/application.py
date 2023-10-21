from sqlalchemy import Column, Integer, BigInteger, String, Text

from db_api.database import Base


class application_table(Base):
    __tablename__ = "Application"

    id = Column(Integer, primary_key=True)
    user_id = Column(BigInteger)
    type = Column(String)
    text = Column(Text)
