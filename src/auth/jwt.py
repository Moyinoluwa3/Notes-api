from datetime import datetime, timedelta

from databases.interfaces import Record
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from src.auth.config import auth_config
from src.auth.exceptions import TokenExpired, InvalidToken
from src.auth.schemas import JWTData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')


def create_access_token(
    *,
    user: Record,
) -> str:
    jwt_data = {
        "sub": str(user["id"]),
        "exp": datetime.utcnow() +  timedelta(minutes=auth_config.JWT_EXP),
        "is_admin": user["is_admin"],
        'scope': 'token'
    }

    return jwt.encode(jwt_data, auth_config.JWT_SECRET, algorithm=auth_config.JWT_ALG)
async def decode_token(self, token):
    try:
        payload = jwt.decode(token, auth_config.JWT_SECRET, algorithms=['HS256'])
        if (payload['scope'] == 'token'):
            return payload['sub']   
        raise InvalidToken()
    except jwt.ExpiredSignatureError:
        raise TokenExpired()