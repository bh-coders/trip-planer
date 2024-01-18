from fastapi import FastAPI
from src.attraction import router

app = FastAPI()



@app.get("/")
def root() -> dict[str, str]:
    return {"Trip": "Planner"}
