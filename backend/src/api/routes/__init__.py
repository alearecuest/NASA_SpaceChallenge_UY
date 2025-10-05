# api/routes/__init__.py
from fastapi import APIRouter
from .asteroids import router as asteroids_router
from .historical import router as historical_router  # ← NUEVO

main_router = APIRouter()
main_router.include_router(asteroids_router, prefix="/asteroids", tags=["asteroids"])
main_router.include_router(historical_router, prefix="/historical", tags=["historical"])  # ← NUEVO

__all__ = ["main_router"]