import uuid
from datetime import datetime, timedelta
from fastapi import Depends
from databases.interfaces import Record
from pydantic import UUID4
from sqlalchemy.orm import Session

from src.auth.config import auth_config
from src.auth.exceptions import InvalidCredentials,UserNotFound,EmailTaken
from src.auth.schemas import AuthUser
from src.auth.security import check_password, hash_password
from src.database import  get_db
from src.models import User
from src.auth.jwt import create_access_token

async def create_user(user: AuthUser,db : Session = Depends(get_db)) -> Record | None:
    email = await db.query(User).filter(User.email == user.email).first()
    if email:
        raise EmailTaken()
    else:
        try:
            hashed_password = hash_password(user.password)
            user.password = hashed_password
            new_user= User(**user.dict())
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
            return new_user
        except Exception as e:
            return {"message" : e}

        

   

def Get_user(id: int,db : Session = Depends(get_db) ):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise UserNotFound()
    return user



async def get_user_by_email(email: str,db : Session = Depends(get_db)) -> Record | None:
    user = await db.query(User).filter(User.email == email).first()
    if not user:
        raise UserNotFound()
    return user


async def authenticate_user(auth_data: AuthUser) -> Record:
    user = await get_user_by_email(auth_data.email)
    if not user:
        raise InvalidCredentials()

    if not check_password(auth_data.password, user["password"]):
        raise InvalidCredentials()
    access_token = create_access_token(user)

    return {"access_token": access_token, "token_type": "bearer"}
    
