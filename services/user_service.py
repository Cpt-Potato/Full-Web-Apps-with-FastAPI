from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto
from sqlalchemy import func
from sqlalchemy.future import select

from data import db_session
from data.user import User


async def user_count() -> int:
    async with db_session.create_async_session() as session:
        result = await session.execute(
            select(func.count(User.id))
        )
        return result.scalar()


async def create_account(name: str, email: str, password: str) -> User:
    user = User()
    user.email = email
    user.name = name
    user.hash_password = crypto.hash(password, rounds=10000)

    async with db_session.create_async_session() as session:
        session.add(user)
        await session.commit()

    return user


async def login_user(email: str, password: str) -> Optional[User]:
    async with db_session.create_async_session() as session:
        result = await session.execute(select(User).filter(User.email == email))
        user = result.scalar_one_or_none()
    try:
        if not crypto.verify(password, user.hash_password):
            return None
    except ValueError:
        return None

    return user


async def get_user_by_id(user_id: int) -> Optional[User]:
    async with db_session.create_async_session() as session:
        result = await session.execute(select(User).filter(User.id == user_id))
        return result.scalar_one_or_none()


async def get_user_by_email(email: str) -> Optional[User]:
    async with db_session.create_async_session() as session:
        result = await session.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()
