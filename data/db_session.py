from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from data.modelbase import SqlAlchemyBase

# __factory: Optional[Callable[[], Session]] = None
db_file = (Path() / "db" / "pypi.sqlite").as_posix()
conn_str = "sqlite:///" + db_file.strip()
engine = create_engine(
    conn_str, echo=False, connect_args={"check_same_thread": False}
)


def global_init():  # db_file: str):
    SqlAlchemyBase.metadata.create_all(engine)
    # global __factory
    #
    # conn_str = "sqlite:///" + db_file.strip()
    # print(f"Connecting to DB with {conn_str}")
    #
    # engine = create_engine(
    #     conn_str, echo=False, connect_args={"check_same_thread": False}
    # )
    # __factory = sessionmaker(bind=engine)
    #
    # # noinspection TaskProblemsInspection
    # import data.__all_models
    #
    # SqlAlchemyBase.metadata.create_all(engine)


def create_session() -> Session:
    with Session(engine) as session:
        session.expire_on_commit = False
        return session

    # session: Session = __factory()
    # return session
