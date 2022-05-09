from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import Session, sessionmaker

from data.modelbase import SqlAlchemyBase

db_file = (Path() / "db" / "pypi.sqlite").as_posix()
conn_str = "sqlite:///" + db_file
async_conn_str = "sqlite+aiosqlite:///" + db_file

engine = create_engine(
    conn_str, echo=True, connect_args={"check_same_thread": False}
)
async_engine = create_async_engine(
    async_conn_str, echo=True, connect_args={"check_same_thread": False},
    future=True
)


async def global_init():
    async with async_engine.begin() as conn:
        await conn.run_sync(SqlAlchemyBase.metadata.create_all)


def create_session() -> Session:
    with Session(engine) as session:
        session.expire_on_commit = False
        return session


def create_async_session() -> AsyncSession:
    async_session = sessionmaker(
        async_engine, expire_on_commit=False, class_=AsyncSession
    )
    return async_session()
