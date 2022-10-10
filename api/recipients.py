from fastapi import APIRouter
from fastapi_sqlalchemy import db
from data.models import Recipient as ModelRecipient
from data.schema import Recipient as SchemaRecipient

router = APIRouter()


@router.get("/api/recipients", tags=["recipients"])
async def get_recipients():
    recipients = db.session.query(ModelRecipient).all()
    return recipients


@router.get("/api/recipients/{recipient_id}", response_model=SchemaRecipient)
async def get_recipient(recipient_id: int):
    recipient = db.session.query(ModelRecipient).get(recipient_id)
    return recipient


@router.post('/api/recipients', response_model=SchemaRecipient)
async def create_recipient(recipient: SchemaRecipient):
    db_recipient = ModelRecipient(name=recipient.name, surname=recipient.surname, age=recipient.age, vat_number=recipient.vat_number)
    db.session.add(db_recipient)
    db.session.commit()
    return db_recipient


@router.delete('/api/recipients/{recipient_id}')
async def delete_recipient(recipient_id: int):
    recipient = db.session.query(ModelRecipient).get(recipient_id)
    db.session.delete(recipient)
