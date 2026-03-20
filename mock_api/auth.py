"""
API key authentication.
Simple but realistic — mirrors how real internal pricing APIs work.
"""

import os
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

API_KEY_HEADER = APIKeyHeader(name="X-API-Key", auto_error=False)

# In production this would be in a secrets manager
# For our project it lives in .env
VALID_API_KEY = os.getenv("PRICING_API_KEY", "dev-pricing-key-12345")


def verify_api_key(api_key: str = Security(API_KEY_HEADER)) -> str:
    if not api_key or api_key != VALID_API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API key",
            headers={"WWW-Authenticate": "ApiKey"},
        )
    return api_key