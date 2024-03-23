from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    lastname = Column(String(40), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(15), nullable=False, unique=True)
    birthday = Column(DateTime)
    data =  Column(String())