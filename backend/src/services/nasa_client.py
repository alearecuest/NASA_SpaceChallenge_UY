import httpx
from config import get_settings

class NasaClient:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = self.settings.NASA_BASE_URL
        self.api_key = self.settings.NASA_API_KEY
    
    async def get_asteroids_feed(self, start_date: str, end_date: str = None):
        """Obtiene asteroides cercanos en un rango de fechas"""
        url = f"{self.base_url}/feed"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "api_key": self.api_key
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()
    
    async def get_asteroid_by_id(self, asteroid_id: str):
        """Obtiene un asteroide específico por ID"""
        url = f"{self.base_url}/neo/{asteroid_id}"
        params = {"api_key": self.api_key}
        
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params=params)
            response.raise_for_status()
            return response.json()

async def get_nasa_client():
    return NasaClient()
