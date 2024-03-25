from faker import Faker
from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date
from sqlalchemy.ext.declarative import declarative_base
from src.database.db import SessionLocal

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

fake = Faker()

db = SessionLocal()

for _ in range(1000):
    try:
        contact = Contact(
            first_name = fake.first_name(),
            last_name = fake.last_name(),
            email = fake.email(),
            phone = fake.phone_number(),
            birthday = fake.date(),
            data = fake.job())
        db.add(contact)
        db.commit()
    except Exception as err:
        db.rollback()
        print(err)
db.close()
