from pydantic import BaseModel
from datetime import date
from typing import List

class InterventionDateBase(BaseModel):
    start_date: date
    end_date: date

class InterventionDateCreate(InterventionDateBase):
    pass

class InterventionDate(InterventionDateBase):
    id: int
    invoice_id: int

    class Config:
        orm_mode = True

class InvoiceBase(BaseModel):
    invoice_number: str
    client: str
    amount_ht: float
    hours_count: int
    days_count: int
    trainer: str
    payment_due: str

class InvoiceCreate(InvoiceBase):
    pass

class Invoice(InvoiceBase):
    id: int
    intervention_dates: List[InterventionDate] = []

    class Config:
        orm_mode = True

class HealthResponse(BaseModel):
    status: str