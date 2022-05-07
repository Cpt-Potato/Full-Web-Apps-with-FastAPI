from datetime import datetime

from sqlalchemy import Column, DateTime, Integer, String, orm

from data.modelbase import SqlAlchemyBase
from data.release import Release


class Package(SqlAlchemyBase):
    __tablename__ = "packages"

    id: str = Column(String, primary_key=True)
    created_date: datetime = Column(DateTime, default=datetime.now, index=True)
    last_updated: datetime = Column(DateTime, default=datetime.now, index=True)
    summary: str = Column(String, nullable=False)
    description: str = Column(String, nullable=False)

    home_page: str = Column(String)
    docs_url: str = Column(String)
    package_url: str = Column(String)

    author_name: str = Column(String)
    author_email: str = Column(String)

    license: str = Column(String)

    releases: list[Release] = orm.relation("Release", order_by=[
        Release.major_ver.desc(),
        Release.minor_ver.desc(),
        Release.build_ver.desc()
    ], back_populates="package")

    def __repr__(self):
        return f"<Package {self.id}>"
