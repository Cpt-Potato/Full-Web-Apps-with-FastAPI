from typing import Optional

from sqlalchemy import func, orm, select

from data import db_session
from data.package import Package
from data.release import Release


async def release_count() -> int:
    async with db_session.create_async_session() as session:
        result = await session.execute(select(func.count(Release.id)))

    return result.scalar()


async def package_count() -> int:
    async with db_session.create_async_session() as session:
        result = await session.execute(select(func.count(Package.id)))

    return result.scalar()


async def latest_releases(limit: int = 5) -> list[Package]:
    async with db_session.create_async_session() as session:
        query = (
            select(Release)
            .options(orm.joinedload(Release.package))
            .order_by(Release.created_date.desc())
            .limit(limit)
        )
        results = await session.execute(query)
        releases = results.scalars()

    return [release.package for release in releases]


async def get_package_by_id(package_name: str) -> Optional[Package]:
    async with db_session.create_async_session() as session:
        result = await session.execute(
            select(Package).filter(Package.id == package_name)
        )

    return result.scalar_one_or_none()


async def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    async with db_session.create_async_session() as session:
        query = (
            select(Release).filter(Release.package_id == package_name)
            .order_by(Release.created_date.desc())
        )
        results = await session.execute(query)

    return results.scalar()
