from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String

from data.modelbase import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = "users"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String)
    email: str = Column(String, unique=True, index=True)
    hashed_password: str = Column(String)
    created_date: datetime = Column(DateTime, default=datetime.now)
    last_login_date: datetime = Column(DateTime, default=datetime.now)
    profile_image_url: str = Column(String)
