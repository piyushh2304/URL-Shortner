from pydantic import BaseModel, HttpUrl, field_validator
from datetime import datetime
from typing import Optional

class URLBase(BaseModel):
    long_url: HttpUrl  # Pydantic validates this is actually a URL

class URLCreate(URLBase):
    custom_alias: Optional[str] = None

    @field_validator("custom_alias")
    @classmethod
    def validate_alias(cls, v):
        if v and not v.isalnum():
            raise ValueError("Alias must be alphanumeric")
        return v

class URLResponse(BaseModel):
    short_code: str
    long_url: str
    short_url: str
    created_at: datetime
    click_count: int = 0

    class Config:
        from_attributes = True  # allows reading from ORM objects