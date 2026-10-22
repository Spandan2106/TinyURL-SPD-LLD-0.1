
import os
import secrets
from contextlib import asynccontextmanager
from pathlib import Path

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, HttpUrl
from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, PyMongoError

BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")
STATIC_DIR = BASE_DIR / "static"


@asynccontextmanager
async def lifespan(app: FastAPI):
    mongo_uri = os.getenv("MONGODB_URI")

    if not mongo_uri:
        raise RuntimeError("MONGODB_URI is missing.")

    client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)

    try:
        client.admin.command("ping")

        database = client["tinyurl"]
        collection = database["urls"]
        collection.create_index("code", unique=True)

        app.state.mongo_client = client
        app.state.urls = collection

        yield
    finally:
        client.close()


app = FastAPI(
    title="TinyURL-SPD-2026",
    description="URL shortener using FastAPI and MongoDB.",
    lifespan=lifespan,
)

app.mount(
    "/static",
    StaticFiles(directory=STATIC_DIR),
    name="static",
)


class URLRequest(BaseModel):
    url: HttpUrl


@app.get("/")
def home():
    return FileResponse(STATIC_DIR / "index.html")


@app.post("/api/urls")
def create_short_url(data: URLRequest, request: Request):
    collection = request.app.state.urls
    original_url = str(data.url)

    try:
        existing = collection.find_one(
            {"original_url": original_url}
        )

        if existing:
            code = existing["code"]
        else:
            for _ in range(10):
                code = secrets.token_urlsafe(6)

                try:
                    collection.insert_one({
                        "code": code,
                        "original_url": original_url,
                    })
                    break
                except DuplicateKeyError:
                    continue
            else:
                raise HTTPException(
                    status_code=500,
                    detail="Could not generate a unique short code.",
                )

    except PyMongoError as exc:
        raise HTTPException(
            status_code=503,
            detail="The database is temporarily unavailable.",
        ) from exc

    short_url = f"{str(request.base_url).rstrip('/')}/{code}"

    return {
        "original_url": original_url,
        "short_url": short_url,
        "code": code,
    }


@app.get("/{code}")
def redirect_to_original(code: str, request: Request):
    collection = request.app.state.urls

    try:
        result = collection.find_one({"code": code})
    except PyMongoError as exc:
        raise HTTPException(
            status_code=503,
            detail="The database is temporarily unavailable.",
        ) from exc

    if result is None:
        raise HTTPException(
            status_code=404,
            detail="Short URL not found.",
        )

    return RedirectResponse(
        url=result["original_url"],
        status_code=302,
    )
