from datetime import datetime
from typing import Optional

from sqlalchemy import orm

from data import db_session
from data.package import Package
from data.release import Release


def release_count() -> int:
    session = db_session.create_session()
    return session.query(Release).count()


def package_count() -> int:
    session = db_session.create_session()
    return session.query(Package).count()


def latest_releases(limit: int = 5) -> list[Package]:
    session = db_session.create_session()
    releases = (
        (
            session.query(Release)
            .options(orm.joinedload(Release.package))
        )
            .order_by(Release.created_date.desc())
            .limit(limit)
            .all()
    )
    return [release.package for release in releases]


def get_package_by_id(package_name: str) -> Optional[Package]:
    session = db_session.create_session()
    return session.query(Package).filter(Package.id == package_name).first()


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    session = db_session.create_session()
    return (
        session.query(Release).filter(Release.package_id == package_name)
        .order_by(Release.created_date.desc()).first()
    )
