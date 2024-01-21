from fastapi import FastAPI, Response
from .cars import create_cars
cars = create_cars(100)  # Здесь хранятся список машин
app = FastAPI()

@app.get("/")
def index():
    return {"message" : "It car API"}


# (сюда писать решение)


# (конец решения)
