import sqlalchemy.exc
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.db_session import get_db
from app.models import users
from app.schemas.users import User, UserCreate

router = APIRouter()


@router.post('/users', response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user = users.create_user(db, user)
    except sqlalchemy.exc.IntegrityError:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="User already exists")

    return user
