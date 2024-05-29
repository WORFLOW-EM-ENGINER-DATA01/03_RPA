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