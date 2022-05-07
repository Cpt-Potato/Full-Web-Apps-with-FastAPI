from datetime import datetime
from typing import Optional

from data import db_session
from data.package import Package
from data.release import Release


def release_count() -> int:
    session = db_session.create_session()
    try:
        return session.query(Release).count()
    finally:
        session.close()


def package_count() -> int:
    return 274_000


def latest_releases(limit: int = 5) -> list:
    return [
        {"id": "fastapi", "summary": "A great web framework"},
        {"id": "uvicorn", "summary": "Your favorite ASGI server"},
        {"id": "httpx", "summary": "Requests for an async world"},
    ][:limit]


def get_package_by_id(package_name: str) -> Optional[Package]:
    package = Package(
        package_name,
        "This is the summary",
        "Full details here!",
        "https://fastapi.tiangolo.com/",
        "MIT",
        "Sebastian Ramirez",
    )
    return package


def get_latest_release_for_package(package_name: str) -> Optional[Release]:
    return Release("1.2.0", datetime.now())
