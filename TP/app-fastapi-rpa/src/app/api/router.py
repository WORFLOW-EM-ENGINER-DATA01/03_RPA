from fastapi import APIRouter, FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine 
from .schemas import Invoice, InterventionDate
from . import models, crud

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
    
@router.get("/intervention_dates", response_model=list[InterventionDate])
def get_all( db: Session = Depends(get_db)):
    invoices = crud.get_all_intervention_dates(db)
    
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