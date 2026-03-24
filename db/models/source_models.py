from sqlalchemy import (
    Column, Numeric, Integer, String, text, TIMESTAMP
)
from sqlalchemy.orm import DeclarativeBase


class SourceBase(DeclarativeBase):
    pass 

class Orders(SourceBase):
    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, nullable=False)
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Numeric(10, 2), nullable=False)
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(TIMESTAMP, nullable=False, server_default=text("NOW()"))
    updated_at = Column(TIMESTAMP, nullable=False, server_default=text("NOW()"))