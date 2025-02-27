from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter() # Initializes a new router instance for handling specific API routes.

# User Entity
class User(BaseModel):
    id: int
    name: str
    lastname: str
    url: str
    age: int

users_list = [User(id=1, name="Oscar", lastname="Ahumada", url="https://ahumada.dev", age=35),
              User(id=2, name="Mateo", lastname="Ahumada", url="https://mate.dev", age=6),
              User(id=3, name="Haakon", lastname="Dalhberg", url="https://haakon.dev", age=23)]


@router.get("/users_json")
async def users_json():
    return [{"name": "Oscar", "Lastname": "Ahumada", "url": "https://ahumada.dev", "age": 35},
            {"name": "Mateo", "Lastname": "Ahumada", "url": "https://mate.dev", "age": 6},
            {"name": "Haakon", "Lastname": "Dalhberg", "url": "https://haakon.dev", "age": 23}]

@router.get("/users")
async def users():
    return users_list
# Path
@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)


# Query
@router.get("/user/")
async def user(id: int):
    return search_user(id)


# http://127.0.0.1:8000/userquery/?id=1


@router.post("/user/", status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="User already exist")
    else:
        users_list.append(user)
        return user

# User to add: {"id": 4,"name": "Oscar", "lastname": "Ahumada", "url": "https://ahumada.dev", "age": 35}

@router.put("/user/")
async def user(user: User):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            return user
    if not found:
        return {"error": "We did not update the user"}
# User to update: {"id": 4,"name": "Dario", "lastname": "Gomez", "url": "https://gomez.dev", "age": 20}


@router.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            return {"User has been deleted"}
    raise HTTPException(status_code=404, detail="User not found")



def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "User not found"}


