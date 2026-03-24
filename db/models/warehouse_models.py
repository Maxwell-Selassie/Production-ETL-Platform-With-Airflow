from sqlalchemy import (
    Column, Numeric, Integer, text, String, TIMESTAMP, Text
)
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.dialects.postgresql import JSONB

class WarehouseBase(DeclarativeBase):
    pass 

class FactOrders(WarehouseBase):
    __tablename__ = "fact_orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    total_amount = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False)
    etl_loaded_at = Column(TIMESTAMP, nullable=False, server_default=text("NOW()"))

class ETLWatermark(WarehouseBase):
    __tablename__ = "etl_watermarks"

    pipeline_name = Column(String(100), primary_key=True)
    last_executed = Column(TIMESTAMP, nullable=False)
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("NOW()"))

