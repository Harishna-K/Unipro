from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
from enum import Enum

class EntityType(str, Enum):
    Customer = "Customer"
    Supplier = "Supplier"

class MasterCreate(BaseModel):
    entity_code: str = Field(..., min_length=1)
    entity_name: str = Field(..., min_length=1)
    addr1: Optional[str]
    addr2: Optional[str]
    type: EntityType
    active: bool = True

class MasterOut(MasterCreate):
    id: int
    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    transaction_number: str
    transaction_date: date
    entity_code: str
    amount: float

class TransactionOut(BaseModel):
    ref_no: str
    ref_date: date
    transaction_number: str
    transaction_date: date
    entity_code: str
    entity_name: str
    type: EntityType
    in_amount: float
    out_amount: float

    class Config:
        orm_mode = True
