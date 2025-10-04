from fastapi import APIRouter, Depends, HTTPException, Query
from services import get_nasa_client, NasaClient
from models import AsteroidFeed

router = APIRouter()

@router.get("/feed", response_model=AsteroidFeed)
async def get_asteroids_feed(
    start_date: str = Query(..., description="Start Date (YYYY-MM-DD)"),
    end_date: str = Query(None, description="End Date (YYYY-MM-DD)"),
    nasa_client: NasaClient = Depends(get_nasa_client)
):
    """Obtener asteroides cercanos en un rango de fechas"""
    try:
        return await nasa_client.get_asteroids_feed(start_date, end_date)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Error fetching NASA data")

@router.get("/{asteroid_id}")
async def get_asteroid(
    asteroid_id: str,
    nasa_client: NasaClient = Depends(get_nasa_client)
):
    """Obtener información de un asteroide específico"""
    try:
        return await nasa_client.get_asteroid_by_id(asteroid_id)
    except httpx.HTTPError as e:
        raise HTTPException(status_code=500, detail="Error fetching asteroid data")