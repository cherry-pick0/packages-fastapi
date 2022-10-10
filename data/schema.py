# build a schema using pydantic
from pydantic import BaseModel


class Package(BaseModel):
    address: str
    weight: int
    recipient_id: int

    class Config:
        orm_mode = True


class Recipient(BaseModel):
    name: str
    surname: str
    vat_number: int
    age: int

    class Config:
        orm_mode = True
