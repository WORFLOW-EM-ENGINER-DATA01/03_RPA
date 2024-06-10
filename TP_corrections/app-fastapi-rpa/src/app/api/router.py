from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine 
from .schemas import Invoice
from . import models, crud
from typing import Union, Dict

app = FastAPI()
router = APIRouter(prefix='/api')

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/invoices", response_model=list[Invoice])
def get_all( db: Session = Depends(get_db)):
    invoices = crud.get_all_invoices(db)
    
    if not invoices:
        raise HTTPException(status_code=404, detail="Aucune facture trouvée")
    return invoices

# /api/invoices/date/2024-05-26/2024-02-15
@router.get("/invoices/date/{start}", response_model=list[Invoice])
def all_intervention_by_start_date( start : str, db: Session = Depends(get_db)):
    invoices = crud.get_all_intervention_by_start_date(start = start, db = db)
    
    return invoices

@router.get("/invoices/date/{year}", response_model=list[Invoice])
def get_invoices_by_date( year: str, db: Session = Depends(get_db)):
    invoices = crud.get_invoices_by_date(year=year, db=db)
    if not invoices:
        raise HTTPException(status_code=404, detail="No invoices found in the given date range")
    
    return invoices

@router.get("/invoices/trainer/{trainer}", response_model=list[Invoice])
def get_invoices_by_date( trainer: str, db: Session = Depends(get_db)):
    invoices = crud.get_invoices_by_trainer(trainer=trainer, db=db)
    if not invoices:
        raise HTTPException(status_code=404, detail="No invoices found in the given date range")
    
    return invoices