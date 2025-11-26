from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from . import crud, schemas, models
from .database import SessionLocal, engine, Base
from typing import List, Optional
from datetime import date

Base.metadata.create_all(bind=engine)
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post('/masters', response_model=schemas.MasterOut)
def create_master(master: schemas.MasterCreate, db: Session = Depends(get_db)):
    existing = crud.get_master_by_code(db, master.entity_code)
    if existing:
        raise HTTPException(status_code=400, detail='Entity code already exists')
    return crud.create_master(db, master)

@router.get('/masters', response_model=List[schemas.MasterOut])
def list_masters(db: Session = Depends(get_db)):
    return crud.list_masters(db)

@router.put('/masters/{code}', response_model=schemas.MasterOut)
def update_master(code: str, patch: schemas.MasterCreate, db: Session = Depends(get_db)):
    m = crud.get_master_by_code(db, code)
    if not m:
        raise HTTPException(status_code=404, detail='Not found')
    return crud.update_master(db, m, patch.dict())

@router.delete('/masters/{code}')
def delete_master(code: str, db: Session = Depends(get_db)):
    m = crud.get_master_by_code(db, code)
    if not m:
        raise HTTPException(status_code=404, detail='Not found')
    crud.delete_master(db, m)
    return {"ok": True}

@router.post('/transactions')
def create_transaction(tx: schemas.TransactionCreate, db: Session = Depends(get_db)):
    try:
        dbtx = crud.create_transaction(db, tx)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    master = dbtx.master
    return {
        'ref_no': dbtx.ref_no,
        'ref_date': dbtx.ref_date,
        'transaction_number': dbtx.transaction_number,
        'transaction_date': dbtx.transaction_date,
        'entity_code': master.entity_code,
        'entity_name': master.entity_name,
        'type': master.type.value,
        'in_amount': dbtx.in_amount,
        'out_amount': dbtx.out_amount,
    }

@router.get('/reports/daily', response_model=List[schemas.TransactionOut])
def report_daily(date_from: Optional[date] = Query(None), date_to: Optional[date] = Query(None), 
                 type: Optional[models.EntityType] = None, entity_code: Optional[str] = None, db: Session = Depends(get_db)):
    txs = crud.report_daily_transactions(db, date_from, date_to, type, entity_code)
    out = []
    for t in txs:
        out.append({
            'ref_no': t.ref_no,
            'ref_date': t.ref_date,
            'transaction_number': t.transaction_number,
            'transaction_date': t.transaction_date,
            'entity_code': t.master.entity_code,
            'entity_name': t.master.entity_name,
            'type': t.master.type.value,
            'in_amount': t.in_amount,
            'out_amount': t.out_amount,
        })
    return out

@router.get('/reports/ledger')
def report_ledger(entity_code: str, date_from: Optional[date] = None, date_to: Optional[date] = None, db: Session = Depends(get_db)):
    txs = crud.ledger_by_entity(db, entity_code, date_from, date_to)
    rows = []
    balance = 0.0
    master = None
    for t in txs:
        master = t.master
        balance += t.in_amount - t.out_amount
        rows.append({
            'ref_no': t.ref_no,
            'ref_date': t.ref_date,
            'transaction_number': t.transaction_number,
            'transaction_date': t.transaction_date,
            'in_amount': t.in_amount,
            'out_amount': t.out_amount,
            'balance': balance,
        })
    return { 'entity_code': entity_code, 'entity_name': master.entity_name if master else None, 'rows': rows }
