from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


class Package(Base):
    __tablename__ = 'package'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    address = Column(String)
    weight = Column(Float)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
    recipient_id = Column(Integer, ForeignKey('recipient.id'), nullable=False)

    recipient = relationship('Recipient')


class Recipient(Base):
    __tablename__ = 'recipient'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    name = Column(String)
    surname = Column(String)
    vat_number = Column(Integer)
    age = Column(Integer)

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
