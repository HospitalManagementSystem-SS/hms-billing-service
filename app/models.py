from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class BillingEvent(Base):
    __tablename__ = "billing_events"
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer)
    patient_id = Column(Integer)
    payload = Column(String(500))
    received_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))

class Invoice(Base):
    __tablename__ = "invoices"
    id = Column(Integer, primary_key=True)
    appointment_id = Column(Integer, unique=True)
    patient_id = Column(Integer)
    amount = Column(Float)
    status = Column(String(50), default="PENDING")
    created_at = Column(DateTime, default=datetime.datetime.now(datetime.UTC))
