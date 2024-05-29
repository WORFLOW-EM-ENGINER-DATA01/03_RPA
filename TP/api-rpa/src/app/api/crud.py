from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from datetime import datetime
from . import models

def get_all_invoices(db: Session):
    return db.query(models.Invoice).all()