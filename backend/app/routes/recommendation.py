from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Purchase

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/best-vendor")
def best_vendor(item: str, required_qty: int, db: Session = Depends(get_db)):
    records = db.query(Purchase).filter(Purchase.item == item).all()

    vendors = {}

    for r in records:
        if abs(r.qty - required_qty) <= required_qty * 0.3:
            vendors.setdefault(r.vendor, []).append(r.price)

    if not vendors:
        return {"message": "No data"}

    avg_prices = {v: sum(p)/len(p) for v, p in vendors.items()}
    best = min(avg_prices, key=avg_prices.get)

    return {"best_vendor": best, "avg_prices": avg_prices}