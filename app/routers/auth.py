from datetime import timedelta
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.dependencies.db_session import get_db
from app.models import users as models
from app.schemas.tokens import Token
from app.schemas.users import UserInDB, User
from app.utils.auth import authenticate_user, get_password_hash, create_access_token, get_current_user
from config import ACCESS_TOKEN_EXPIRE_MINUTES

router = APIRouter()


@router.post("/register", response_model=User)
def register(
        user: UserInDB,
        db: Annotated[Session, Depends(get_db)]
):
    userdb = models.User()
    userdb.username = user.username
    userdb.password = get_password_hash(user.password)
    userdb.email = user.email
    userdb.first_name = user.first_name
    userdb.last_name = user.last_name

    db.add(userdb)
    db.commit()
    return userdb


@router.post("/token", response_model=Token)
async def login_for_access_token(
        user: UserInDB,
        db: Annotated[Session, Depends(get_db)]
):
    user = authenticate_user(user, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token_expires = timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=User)
def get_logged_user(user: Annotated[models.User, Depends(get_current_user)]):
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return user
