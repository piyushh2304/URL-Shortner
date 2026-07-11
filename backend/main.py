from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from models import URLCreate, URLResponse
from database import get_db
import crud

app = FastAPI(title="URL Shortener")

# Allow your React dev server to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_URL = "http://localhost:8000"

@app.post("/shorten", response_model=URLResponse)
def shorten_url(payload: URLCreate, db: Session = Depends(get_db)):
    db_url = crud.create_url(db, str(payload.long_url), payload.custom_alias)
    return URLResponse(
        short_code=db_url.short_code,
        long_url=db_url.long_url,
        short_url=f"{BASE_URL}/{db_url.short_code}",
        created_at=db_url.created_at,
        click_count=db_url.click_count,
    )

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    crud.increment_click(db, db_url)
    return RedirectResponse(url=db_url.long_url)

@app.get("/api/stats/{short_code}", response_model=URLResponse)
def get_stats(short_code: str, db: Session = Depends(get_db)):
    db_url = crud.get_url(db, short_code)
    if not db_url:
        raise HTTPException(status_code=404, detail="Short URL not found")
    return URLResponse(
        short_code=db_url.short_code,
        long_url=db_url.long_url,
        short_url=f"{BASE_URL}/{db_url.short_code}",
        created_at=db_url.created_at,
        click_count=db_url.click_count,
    )