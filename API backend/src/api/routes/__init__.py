from fastapi import APIRouter
from .asteroids import router as asteroids_router


# Combina todos los routers
main_router = APIRouter()
main_router.include_router(asteroids_router, prefix="/asteroids", tags=["asteroids"])

__all__ = ["main_router"]