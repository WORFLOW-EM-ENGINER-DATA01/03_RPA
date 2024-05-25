from sqlalchemy import Date, Column, ForeignKey, Integer, String, Numeric
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from .database import Base

class InterventionDate(Base):
    __tablename__ = "intervention_dates"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_id = Column(Integer, ForeignKey("invoices.id"))
    start_date = Column(Date)
    end_date = Column(Date)
    invoice = relationship("Invoice", back_populates="intervention_dates")

class Invoice(Base):
    __tablename__ = "invoices"
    
    id = Column(Integer, primary_key=True, index=True)
    invoice_number = Column(String, unique=True, index=True)
    client = Column(String, index=True)
    amount_ht = Column(Numeric(10, 2))
    hours_count = Column(Integer)
    days_count = Column(Integer)
    trainer = Column(String)
    payment_due = Column(String)
    intervention_dates = relationship("InterventionDate", back_populates="invoice")
