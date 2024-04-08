from fastapi import FastAPI

from entities.user import User
from adapters.create_user import create_user

app = FastAPI()


@app.get("/")
def read_root():
    return {"Introduction": "to Clean Architecture"}


@app.post("/user")
def add_user(user: User):
    return create_user(user)