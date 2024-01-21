from fastapi import FastAPI

from src.attraction.routes.router import router as attraction_router
from src.auth.routes.router import router as auth_router
from src.database import engine, Base
from src.attraction.models import Attraction  # Importuj tutaj wszystkie swoje modele


Base.metadata.create_all(bind=engine)
app = FastAPI()

app.include_router(attraction_router, prefix="/attractions")
app.include_router(auth_router, prefix="/auth")
