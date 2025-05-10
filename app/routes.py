from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Invoice

router = APIRouter()

@router.get("/invoices/{id}")
def get_invoice(id: int, db: Session = Depends(get_db)):
    invoice = db.query(Invoice).filter(Invoice.id == id).first()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice

@router.get("/invoices")
def get_all_invoices(db: Session = Depends(get_db)):
    invoice = db.query(Invoice).all()
    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")
    return invoice
