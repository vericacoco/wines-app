from pydantic import BaseModel

class Wine(BaseModel):
    name: str
    country: str
    type: str
    price: float
    description: str | None = None
