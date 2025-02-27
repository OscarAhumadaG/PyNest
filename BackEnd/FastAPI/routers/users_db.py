from fastapi import APIRouter, HTTPException, status, Query
from db.models.user import User
from db.schemas.user import user_schema, users_schema
from db.client import db_client
from bson import ObjectId, errors


router = APIRouter(prefix="/userdb",
                   tags=["userdb"],
                   responses={status.HTTP_404_NOT_FOUND: {"message": "Not Found"}})


@router.get("/", response_model=list[User])
async def users():
    return users_schema(db_client.local.users.find())



@router.get("/{id}")  # Path
async def user(id: str):
    return search_user("_id", ObjectId(id))


@router.get("/search/")  # Query Parameter
async def user(id: str):
    user_data = search_user("_id", ObjectId(id))

    if not user_data:
        raise HTTPException(status_code=404, detail="User not found")

    return user_data

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def user(user: User):
    if type(search_user("email", user.email)) == User:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User already exist")

    user_dict = dict(user)
    del user_dict["id"]

    id = db_client.local.users.insert_one(user_dict).inserted_id

    new_user = user_schema(db_client.local.users.find_one({"_id": id}))

    return User(**new_user)

@router.put("/", response_model=User)
async def user(user: User):
    user_dict = user.model_dump(exclude={"id"})

    query_filter = {"_id": ObjectId(user.id)}
    update_operation = {"$set": user_dict}

    try:
        updated_user = db_client.local.users.update_one(query_filter, update_operation)

        if updated_user.matched_count == 0:  # System was unable to find the user
            raise HTTPException(status_code=404, detail="User not found")
        if updated_user.modified_count == 0:  # We dont make any changes
            raise HTTPException(status_code=400, detail="User has laready these values")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error trying to update the user: {str(e)}")

    return search_user("_id", ObjectId(user.id))



@router.delete("/{id}", status_code=status.HTTP_200_OK)
async def delete_user(id: str):
    try:
        # Convert the string id to ObjectId
        str_id = str(id)
        object_id = ObjectId(str_id)

        # Attempt to delete the user from the collection
        result = db_client.local.users.delete_one({"_id": object_id})

        # Check if any user was deleted
        if result.deleted_count == 0:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return {"message": "User deleted successfully"}

    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting user: {str(e)}"
        )


def search_user(field: str, key):
    try:
        if field == "_id":
            key = ObjectId(key)  # Convert string to ObjectId
        user = db_client.local.users.find_one({field: key})
        return User(**user_schema(user)) if user else None
    except Exception as e:
        return None