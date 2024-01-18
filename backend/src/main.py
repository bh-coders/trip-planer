from fastapi import FastAPI
from src.attraction import router

app = FastAPI()

app.include_router(router.router, prefix="/attractions")


@app.get("/")
def root() -> dict[str, str]:
    return {"Trip": "Planner"}

