from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

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
    "password": "123456"
    },
    "mateoar": {
    "username": "mateoar",
    "full_name": "Mateo Ahumada",
    "email": "mateo0127@gmail.com",
    "disabled": True,
    "password": "789456"
    }}

def search_userdb(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    if username in users_db:
        return User(**users_db[username])

async def current_user(token: str = Depends(oauth2)):
    user =  search_user(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credential",
            headers={"WWW-Authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user",
            headers={"WWW-Authenticate": "Bearer"})
    return user


@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="User not found")
    user = search_userdb(form.username)
    if not user or form.password != user.password:
        raise HTTPException(
            status_code=400, detail="Password is not correct")
    return {"access_token": user.username, "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user