from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
# to get a string like this run:
# openssl rand -hex 32
SECRET = "455b8f46b6870d552b150290388200914bb1279192aa4f4b091776f9e6b33294"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str


users_db = {
    "oahumada": {
    "username": "oahumada",
    "full_name": "Oscar Ahumada",
    "email": "odahumada26@gmail.com",
    "disabled": False,
    "password": "$2a$12$wmml.O8ASK0YIHy2QSNhH.WbVywsTbtWQ8YjQx1kQfXmHvIsqlz52" # 12345
    },
    "mateoar": {
    "username": "mateoar",
    "full_name": "Mateo Ahumada",
    "email": "mateo0127@gmail.com",
    "disabled": True,
    "password": "$2a$12$CD.CZSyxHqwdWnrdJ8iwUOq9B4W0y20w3x1CFKrV6f92FNNeaQTbu" # 45678
    }}

def search_userdb(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def auth_user(token: str = Depends(oauth2)):

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credential",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise exception
    except (InvalidTokenError, jwt.ExpiredSignatureError, jwt.DecodeError):
        raise exception

    return search_user(username)



async def current_user(user: User = Depends(auth_user)):

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"})
    return user

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="User not found")
    user = search_userdb(form.username)

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=400, detail="Password is not correct")

    access_token = {"sub": user.username, "exp": datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_DURATION)}


    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "Bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user