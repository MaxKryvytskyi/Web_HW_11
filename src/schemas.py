from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field


class ContactBase(BaseModel):
    name: str = Field(max_length=40)
    lastname: str = Field(max_length=40)
    email: str = Field(max_length=50)
    phone: str = Field(max_length=15)
    birthday: datetime
    data: str


# class ContactUpdate(ContactBase):
#     id: int

# class ContactDataUpdate(ContactModel):
#     data: str


class ContactResponse(ContactBase):
    id: int

    class Config:
        orm_mode = True
