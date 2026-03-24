"""
Pydantic response models — defines the API contract.
This is what our extractor will deserialize into.
"""

from datetime import datetime
from pydantic import BaseModel


class ProductPrice(BaseModel):
    product_id:     int
    name:           str
    category:       str
    base_price:     float
    current_price:  float
    snapshotted_at: str


class PaginatedPriceResponse(BaseModel):
    total:    int
    page:     int
    per_page: int
    pages:    int
    data:     list[ProductPrice]


class SingleProductResponse(BaseModel):
    data: ProductPrice