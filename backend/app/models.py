from sqlalchemy import Column, Integer, String, Date, Float, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class EntityType(str, enum.Enum):
    Customer = "Customer"
    Supplier = "Supplier"

class Master(Base):
    __tablename__ = "masters"
    id = Column(Integer, primary_key=True, index=True)
    entity_code = Column(String, unique=True, index=True, nullable=False)
    entity_name = Column(String, nullable=False)
    addr1 = Column(String, nullable=True)
    addr2 = Column(String, nullable=True)
    type = Column(Enum(EntityType), nullable=False)
    active = Column(Boolean, default=True)
    transactions = relationship("Transaction", back_populates="master")

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    ref_no = Column(String, unique=True, index=True, nullable=False)
    ref_date = Column(Date, server_default=func.current_date())
    transaction_number = Column(String, nullable=False)
    transaction_date = Column(Date, nullable=False)
    master_id = Column(Integer, ForeignKey("masters.id"))
    amount = Column(Float, nullable=False)
    in_amount = Column(Float, default=0.0)
    out_amount = Column(Float, default=0.0)

    master = relationship("Master", back_populates="transactions")
