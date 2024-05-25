from sqlalchemy.orm import Session

from . import models, schemas

def get_all_invoices(db: Session):
    return db.query(models.Invoice).all()


def get_invoice_by_id(db: Session, id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == id).first()

def get_all_intervention_dates(db: Session):
    return db.query(models.InterventionDate).all()

