from fastapi import FastAPI

from .routes import games_router


app = FastAPI()


app.include_router(games_router)
