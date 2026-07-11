# crud.py
import string, random
from sqlalchemy.orm import Session
from database import URLModel

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))

def create_url(db: Session, long_url: str, custom_alias: str = None):
    code = custom_alias or generate_short_code()
    # ensure uniqueness
    while db.query(URLModel).filter(URLModel.short_code == code).first():
        code = generate_short_code()

    db_url = URLModel(short_code=code, long_url=long_url)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url(db: Session, short_code: str):
    return db.query(URLModel).filter(URLModel.short_code == short_code).first()

def increment_click(db: Session, db_url: URLModel):
    db_url.click_count += 1
    db.commit()