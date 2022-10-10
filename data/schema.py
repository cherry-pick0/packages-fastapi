# build a schema using pydantic
from typing import Optional

from pydantic import BaseModel


class Package(BaseModel):
    id: Optional[int] = None
    address: str
    weight: int
    recipient_id: int

    class Config:
        orm_mode = True


class Recipient(BaseModel):
    id: Optional[int] = None
    name: str
    surname: str
    vat_number: int
    age: int

    class Config:
        orm_mode = True
