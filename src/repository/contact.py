from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactUpdate, ContactBase, ContactDataUpdate


async def get_contacts(skip: int, limit: int, db: Session):
    contacts = db.query(Contact).offset(skip).limit(limit).all()
    return contacts


async def get_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id==contact_id).first()
    return contact


async def create_contact(body: ContactBase, db: Session):
    contact = Contact(
        first_name = body.first_name,
        last_name = body.last_name,
        email = body.email,
        phone = body.phone,
        birthday = body.birthday,
        data = body.data
    )
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id: int, body: ContactUpdate, db: Session):
    contact = db.query(Contact).filter(Contact.id==contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        contact.data = body.data
        db.commit()
    return contact


async def update_data_contact(contact_id: int, body: ContactDataUpdate, db: Session):
    contact = db.query(Contact).filter(Contact.id==contact_id).first()
    if contact:
        contact.data = body.data
        db.commit()
    return contact


async def remove_contact(contact_id: int, db: Session):
    contact = db.query(Contact).filter(Contact.id==contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact