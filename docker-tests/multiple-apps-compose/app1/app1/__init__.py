from fastapi import FastAPI
from fastapi import APIRouter

version="v1"
app = FastAPI(version=version, title="My API", description="My API description")

messages = {
    "1": "Hello World",
    "2": "Hello FastAPI",
    "3": "Hello Python"
}


message_router = APIRouter()

@message_router.get("/")
async def read_root(message_id: str):

    message = messages.get(message_id, None)
    if message is None:
        return {"message": "Message not found"}
    else:
        return {"message": messages[message_id]}
    
app.include_router(message_router, prefix="/message", tags=["message"])
    

    