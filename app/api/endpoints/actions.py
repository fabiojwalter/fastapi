from fastapi import APIRouter, Depends
from auth import validate_api_token

router = APIRouter()

@router.get("/")
async def action(api_key : str = Depends(validate_api_token)):
    return {"module": "actions granted"}