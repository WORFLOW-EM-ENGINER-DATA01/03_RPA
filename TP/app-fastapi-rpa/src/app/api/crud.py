from sqlalchemy.orm import Session

from . import models, schemas

def get_all_invoices(db: Session):
    return db.query(models.Invoice).all()

def get_invoice_by_id(db: Session, id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == id).first()

def get_all_intervention_dates(db: Session):
    return db.query(models.InterventionDate).all()

def get_invoices_by_date(year : str, db : Session) :
    
    return db.query(models.Invoice).join(models.InterventionDate).filter(
            models.InterventionDate.start_date == year
    ).all()
    
def get_invoices_by_trainer(trainer : str, db : Session) :
    
    return db.query(models.Invoice).filter(
            models.Invoice.trainer == trainer
    ).all()