# auth.py
import os
from fastapi import Depends, HTTPException
from fastapi.security import APIKeyHeader

# API token header
API_KEY_HEADER = APIKeyHeader(name="X-API-KEY", auto_error=False)

# Check if the API token is valid
def validate_api_token(api_key: str = Depends(API_KEY_HEADER)):
    api_token = os.getenv("API_TOKEN")
    if api_key != api_token:
        raise HTTPException(status_code=401, detail="Invalid API token")
    return True