import bcrypt
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import Session

from app.db.base import Base
from app.models.base import BaseDBModel
from app.schemas import users as schemas


class User(Base, BaseDBModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String, unique=True, index=True)
    password = Column(String)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)


def get_user(db: Session, phone_number: str) -> User | None:
    db_user = db.query(User).filter_by(phone_number=phone_number).first()
    return db_user


def create_user(db: Session, user: schemas.UserCreate, is_admin: bool = False) -> User:
    password = bcrypt.hashpw(user.password.encode('utf-8'), bcrypt.gensalt())
    db_user = User(
        password=password,
        first_name=user.first_name,
        last_name=user.last_name,
        phone_number=user.phone_number,
        is_admin=is_admin
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
