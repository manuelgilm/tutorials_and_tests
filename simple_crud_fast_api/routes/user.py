from fastapi import APIRouter

from models.users import UserList
from models.users import User

user_router = APIRouter(prefix="/users", tags=["users"])

@user_router.get("/list/")
async def list_users():
    user_list = []  
    users=[
        {"first_name": "John", "last_name": "Doe", "email": "some@gmail.com"},
        {"first_name": "Jane", "last_name": "Doe", "email": "some2@gmail.com"},
    ]
    for user in users:
        user_list.append(User.model_validate(user))

    return UserList(users=user_list).model_dump()

# Create a new user 
@user_router.post("/register/")
async def register_user(user: User):
    return user.model_dump()

# Retrieve a user by name
@user_router.get("/get/{user_name}")
async def get_user(user_name: str):
    return {"user_name": user_name} 

# Update a user by name
@user_router.put("/update/{user_name}")
async def update_user(user_name: str, user: User):
    return {"user_name": user_name, "user": user.dict()}

# Delete a user by name
@user_router.delete("/delete/{user_name}")
async def delete_user(user_name: str):
    return {"user_name": user_name}