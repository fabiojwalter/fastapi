from fastapi import APIRouter

from api.endpoints import healthcheck, actions
router = APIRouter()

api_router = APIRouter()
api_router.include_router(healthcheck.router, prefix="/v1/health-check", tags=["health-check"])
api_router.include_router(actions.router, prefix="/v1/actions", tags=["actions"])