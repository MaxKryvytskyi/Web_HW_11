from datetime import date
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    first_name: str = Field(max_length=40)
    last_name: str = Field(max_length=40)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=13)
    birthday: date 
    data: str = Field(max_length=250)


class ContactUpdate(ContactBase):
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date 
    data: str

class ContactDataUpdate(BaseModel):
    data: str


class ContactResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    phone: str
    birthday: date 
    data: str

    class Config:
        orm_mode = True
