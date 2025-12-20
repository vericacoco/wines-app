from pydantic import BaseModel
from typing import Optional

class Wine(BaseModel):
    name: str
    country: str
    type: str
    price: float
    description: Optional[str] = None
