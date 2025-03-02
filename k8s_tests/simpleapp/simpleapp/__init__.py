from fastapi import FastAPI 

app = FastAPI()


@app.get("/")
async def check():
    return {"message": "Hello World"}

