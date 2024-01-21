from fastapi import FastAPI, Response
from .users import create_users

users = create_users(100)  # Здесь хранятся список пользователей
app = FastAPI()
@app.get("/")
def index(request: Request):
    return {"message": "It is user API"}

# (сюда писать решение)

# (конец решения)
