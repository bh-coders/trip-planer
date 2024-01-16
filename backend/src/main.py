from fastapi import FastAPI
from attraction import router

app = FastAPI()

app.include_router(router.router, prefix="/attractions")

@app.get("/")
def root():
    return {"Trip": "Planner"}

