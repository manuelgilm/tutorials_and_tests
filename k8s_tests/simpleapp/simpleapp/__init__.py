from fastapi import FastAPI 
import os 
app = FastAPI()


@app.get("/")
async def check():
    some = os.getenv("SOME_ENV", None)
    return {"message": "Hello World", "SOME_ENV": some}

