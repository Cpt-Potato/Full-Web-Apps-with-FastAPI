from datetime import datetime

from sqlalchemy import (BigInteger, Column, DateTime,
                        ForeignKey, Integer, String, orm)

from data.modelbase import SqlAlchemyBase


class Release(SqlAlchemyBase):
    __tablename__ = "releases"

    id: int = Column(Integer, primary_key=True, autoincrement=True)

    major_ver: int = Column(BigInteger, index=True)
    minor_ver: int = Column(BigInteger, index=True)
    build_ver: int = Column(BigInteger, index=True)

    created_date: datetime = Column(DateTime, default=datetime.now, index=True)
    comment: str = Column(String)
    url: str = Column(String)
    size: int = Column(BigInteger)

    package_id: str = Column(String, ForeignKey("packages.id"))
    package = orm.relation("Package")

    @property
    def version_text(self):
        return f"{self.major_ver}, {self.minor_ver}, {self.build_ver}"
