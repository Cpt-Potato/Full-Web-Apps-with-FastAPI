from typing import Optional

from passlib.handlers.sha2_crypt import sha512_crypt as crypto

from data import db_session
from data.user import User


def user_count() -> int:
    session = db_session.create_session()
    return session.query(User).count()


def create_account(name: str, email: str, password: str) -> User:
    session = db_session.create_session()

    user = User()
    user.email = email
    user.name = name
    user.hash_password = crypto.hash(password, rounds=10000)

    session.add(user)
    session.commit()

    return user


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()
    user = session.query(User).filter(User.email == email).first()
    if not crypto.verify(password, user.hash_password):
        return None
    return user


def get_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.id == user_id).first()


def get_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()
    return session.query(User).filter(User.email == email).first()
