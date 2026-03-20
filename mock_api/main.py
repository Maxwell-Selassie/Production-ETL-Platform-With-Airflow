"""
Mock Pricing Service API.
Simulates an internal pricing microservice.

Endpoints:
    GET /health                      — health check
    GET /api/v1/prices               — paginated list of all product prices
    GET /api/v1/prices/{product_id}  — single product price
"""

import math
import logging
from fastapi import FastAPI, Depends, Query, HTTPException

from auth import verify_api_key
from data import get_all_products_with_prices, get_product_by_id
from models import PaginatedPriceResponse, SingleProductResponse, ProductPrice

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

app = FastAPI(
    title="Grocery Pricing Service",
    description="Internal pricing API — daily product price snapshots",
    version="1.0.0",
)


@app.get("/health")
def health_check():
    """Used by Docker healthcheck and Airflow to verify API is up."""
    return {"status": "healthy", "service": "pricing-api"}


@app.get(
    "/api/v1/prices",
    response_model=PaginatedPriceResponse,
    dependencies=[Depends(verify_api_key)],
)
def get_all_prices(
    page: int = Query(default=1, ge=1, description="Page number"),
    per_page: int = Query(default=10, ge=1, le=25, description="Results per page"),
):
    """
    Returns paginated daily price snapshots for all products.
    Pagination is intentional — mirrors real APIs that never
    return all records in one call.
    """
    all_products = get_all_products_with_prices()
    total = len(all_products)
    pages = math.ceil(total / per_page)

    if page > pages:
        raise HTTPException(status_code=404, detail=f"Page {page} does not exist")

    start = (page - 1) * per_page
    end = start + per_page
    paginated = all_products[start:end]

    log.info(f"Serving prices — page {page}/{pages}, {len(paginated)} products")

    return PaginatedPriceResponse(
        total=total,
        page=page,
        per_page=per_page,
        pages=pages,
        data=[ProductPrice(**p) for p in paginated],
    )


@app.get(
    "/api/v1/prices/{product_id}",
    response_model=SingleProductResponse,
    dependencies=[Depends(verify_api_key)],
)
def get_single_price(product_id: int):
    """Returns current price for a single product."""
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail=f"Product {product_id} not found")
    return SingleProductResponse(data=ProductPrice(**product))