from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import datetime
from . import models

def get_all_invoices(db: Session):
    return db.query(models.Invoice).all()

def get_invoice_by_id(db: Session, id: int):
    return db.query(models.Invoice).filter(models.Invoice.id == id).first()

def get_all_intervention_by_start_date(db: Session, start : str ):
    
    sql_query = """
        SELECT *
        FROM invoices
        WHERE intervention_dates->>'start_date' = :start_date
    """
    # Exécuter la requête SQL avec les paramètres
    result = db.execute(text(sql_query), {"start_date": start})
    # Récupérer les résultats
    invoices = result.fetchall()
    
    return invoices
 
def get_invoices_by_date(year : str, db : Session) :
    
    return db.query(models.Invoice).all()
    
def get_invoices_by_trainer(trainer : str, db : Session) :
    
    return db.query(models.Invoice).filter(
            models.Invoice.trainer == trainer
    ).all()