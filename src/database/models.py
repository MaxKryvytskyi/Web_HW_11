from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(40), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone = Column(String(20), nullable=False, unique=True)
    birthday = Column(Date)
    data =  Column(String(250))