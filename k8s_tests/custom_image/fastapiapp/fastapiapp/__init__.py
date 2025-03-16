from fastapi import FastAPI
from util_package.main import say_something
app = FastAPI()

@app.get("/")
def read_root():
    say_something()
    return {"message": "Hello World"}
