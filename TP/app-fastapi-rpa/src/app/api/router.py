from fastapi import APIRouter, FastAPI, Depends
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
    
    return invoices

@router.get("/intervention_dates", response_model=list[InterventionDate])
def get_all( db: Session = Depends(get_db)):
    invoices = crud.get_all_intervention_dates(db)
    
    return invoices

# TODO les autres routes