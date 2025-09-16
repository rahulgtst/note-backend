from fastapi import FastAPI
from .routes import auth, notes
from .database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Notes API")

app.include_router(auth.router)
app.include_router(notes.router)
