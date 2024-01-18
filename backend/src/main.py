from fastapi import FastAPI
from attraction.routes.router import router as attraction_router
from database import engine, Base
from attraction.models import Attraction  # Importuj tutaj wszystkie swoje modele


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(attraction_router, prefix="/attractions")
