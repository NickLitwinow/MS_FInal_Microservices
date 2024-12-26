import random
import string

from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

import models
from database import get_db, create_tables

app = FastAPI(
    title="Short URL Service",
    description="Сервис для сокращения длинных URL и их редиректа.",
    version="1.0.0"
)

create_tables()


class URLRequest(BaseModel):
    url: str

class URLResponse(BaseModel):
    short_id: str
    full_url: str


def generate_short_id(length=6) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


@app.post("/shorten", response_model=URLResponse)
def create_short_url(data: URLRequest):
    db = get_db()

    full_url_str = data.url

    existing = db.query(models.ShortURL).filter_by(full_url=full_url_str).first()
    if existing:
        return URLResponse(short_id=existing.short_id, full_url=existing.full_url)

    short_id = generate_short_id()
    while db.query(models.ShortURL).filter_by(short_id=short_id).first():
        short_id = generate_short_id()

    new_record = models.ShortURL(
        short_id=short_id,
        full_url=full_url_str
    )
    db.add(new_record)
    db.commit()
    db.refresh(new_record)

    return URLResponse(short_id=new_record.short_id, full_url=new_record.full_url)


@app.get("/{short_id}", response_model=URLResponse)
def redirect_to_full_url(short_id: str):
    db = get_db()
    record = db.query(models.ShortURL).filter(models.ShortURL.short_id == short_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Short URL not found.")

    return RedirectResponse(url=record.full_url)


@app.get("/stats/{short_id}", response_model=URLResponse)
def get_stats(short_id: str):
    db = get_db()
    record = db.query(models.ShortURL).filter(models.ShortURL.short_id == short_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Short URL not found.")

    return URLResponse(short_id=record.short_id, full_url=record.full_url)
