from sqlalchemy.orm import Session
from . import models, schemas
from datetime import date

_daily_counters = {}

def get_master_by_code(db: Session, code: str):
    return db.query(models.Master).filter(models.Master.entity_code == code).first()

def list_masters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Master).offset(skip).limit(limit).all()

def create_master(db: Session, master: schemas.MasterCreate):
    dbm = models.Master(**master.dict())
    db.add(dbm)
    db.commit()
    db.refresh(dbm)
    return dbm

def update_master(db: Session, db_master: models.Master, patch: dict):
    for k, v in patch.items():
        setattr(db_master, k, v)
    db.add(db_master)
    db.commit()
    db.refresh(db_master)
    return db_master

def delete_master(db: Session, db_master: models.Master):
    db.delete(db_master)
    db.commit()
    return True

def _generate_ref_no(tx_date: date):
    key = tx_date.isoformat()
    _daily_counters.setdefault(key, 0)
    _daily_counters[key] += 1
    seq = _daily_counters[key]
    return f"TR-{tx_date.strftime('%Y%m%d')}-{seq:04d}"

def create_transaction(db: Session, tx: schemas.TransactionCreate):
    master = db.query(models.Master).filter(models.Master.entity_code == tx.entity_code, models.Master.active == True).first()
    if not master:
        raise ValueError("Entity not found or inactive")

    if master.type.value == "Customer":
        in_amount = tx.amount
        out_amount = 0.0
    else:
        in_amount = 0.0
        out_amount = tx.amount

    ref_no = _generate_ref_no(tx.transaction_date)
    dbtx = models.Transaction(
        ref_no=ref_no,
        ref_date=tx.transaction_date,
        transaction_number=tx.transaction_number,
        transaction_date=tx.transaction_date,
        master_id=master.id,
        amount=tx.amount,
        in_amount=in_amount,
        out_amount=out_amount,
    )
    db.add(dbtx)
    db.commit()
    db.refresh(dbtx)
    return dbtx

def report_daily_transactions(db: Session, date_from=None, date_to=None, type_filter=None, entity_code=None):
    q = db.query(models.Transaction).join(models.Master)
    if date_from:
        q = q.filter(models.Transaction.transaction_date >= date_from)
    if date_to:
        q = q.filter(models.Transaction.transaction_date <= date_to)
    if type_filter:
        q = q.filter(models.Master.type == type_filter)
    if entity_code:
        q = q.filter(models.Master.entity_code == entity_code)
    q = q.order_by(models.Transaction.transaction_date)
    return q.all()

def ledger_by_entity(db: Session, entity_code: str, date_from=None, date_to=None):
    q = db.query(models.Transaction).join(models.Master).filter(models.Master.entity_code == entity_code)
    if date_from:
        q = q.filter(models.Transaction.transaction_date >= date_from)
    if date_to:
        q = q.filter(models.Transaction.transaction_date <= date_to)
    q = q.order_by(models.Transaction.transaction_date)
    return q.all()
