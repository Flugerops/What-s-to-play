from os import getenv
from requests import get

from fastapi import APIRouter
from dotenv import load_dotenv


games_router = APIRouter(prefix="/games")
load_dotenv()
API_KEY = getenv("API_KEY")


@games_router.get("/search/")
async def get_byname(search: str, page: int, page_size: int):
    url = "https://api.rawg.io/api/games"
    params = {"key": API_KEY, "search": search, "page": page, "page_size": page}
    response = get(url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error {response.status_code}"
