from pydantic import BaseModel, HttpUrl, Field
from datetime import datetime


class URLCreate(BaseModel):
    url: HttpUrl = Field(max_length=2048)

class URLResponse(BaseModel):
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}

class URLStats(BaseModel):
    url: str
    short_code: str
    created_at: datetime
    updated_at: datetime
    access_count: int

    model_config = {"from_attributes": True}