import httpx
import math
import os
from dotenv import load_dotenv
from models.schemas_neo import NeoData, NasaNeoWSResponse

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY")
NASA_NEOWS_URL = f"https://api.nasa.gov/neo/rest/v1/neo/{{asteroid_id}}?api_key={NASA_API_KEY}"

# Densidad por defecto para asteroides rocosos (kg/m³)
DEFAULT_DENSITY = 2500

async def get_neo_data(asteroid_id: str) -> NeoData:
    """
    Obtiene y filtra datos de un asteroide desde la API NeoWS de la NASA,
    enfocándose unicamente en las aproximaciones a la Tierra.
    """
    if not NASA_API_KEY:
        raise ValueError("Error: La variable de entorno NASA_API_KEY no está configurada.")

    async with httpx.AsyncClient() as client:
        response = await client.get(NASA_NEOWS_URL.format(asteroid_id=asteroid_id))
        
        if response.status_code != 200:
            print(f"Respuesta de la API de la NASA: STATUS {response.status_code}")
            raise ValueError(f"Error al obtener datos de la NASA para {asteroid_id}: {response.text}")
        
        try:
            nasa_data = NasaNeoWSResponse(**response.json())
        except Exception as e:
            print(f"Error parseando JSON de la NASA: {e}")
            raise ValueError(f"No se pudo parsear la respuesta de la NASA: {e}")

    earth_approaches = [
        approach for approach in nasa_data.close_approach_data 
        if approach.orbiting_body.lower() == "earth"
    ]

    if not earth_approaches:
        print(f"El asteroide {asteroid_id} no tiene aproximaciones a la tierra")
        raise ValueError(f"El asteroide {asteroid_id} no tiene aproximaciones registradas a la Tierra.")

    closest_approach = min(
        earth_approaches, 
        key=lambda a: float(a.miss_distance.kilometers)
    )

    name = nasa_data.name
    designation = nasa_data.designation
    diameter_min_m = nasa_data.estimated_diameter.meters['estimated_diameter_min']
    diameter_max_m = nasa_data.estimated_diameter.meters['estimated_diameter_max']
    
    distance_km = float(closest_approach.miss_distance.kilometers)
    velocity_km_s = float(closest_approach.relative_velocity.kilometers_per_second)
    
    is_hazardous = nasa_data.is_potentially_hazardous_asteroid

    avg_diameter_m = (diameter_min_m + diameter_max_m) / 2
    volume_m3 = (4/3) * math.pi * ((avg_diameter_m / 2) ** 3)
    mass_kg = volume_m3 * DEFAULT_DENSITY
    energia_joules = 0.5 * mass_kg * ((velocity_km_s * 1000) ** 2)

    peligrosidad = "Asteroide potencialmente peligroso" if is_hazardous else "Riesgo bajo"
    
    riesgo_torino = 1 if is_hazardous else 0
    riesgo_palermo = -1.0 if is_hazardous else -5.0
    
    composicion = f"No disponible en esta API (densidad asumida: {DEFAULT_DENSITY} kg/m³)"

    return NeoData(
        nombre=name,
        designacion=designation,
        size=avg_diameter_m,
        distancia_actual_km=distance_km,
        velocidad_relativa_km_s=velocity_km_s,
        riesgo_torino=riesgo_torino,
        riesgo_palermo=riesgo_palermo,
        composicion_estimada=composicion,
        energia_impacto_joules=energia_joules,
        peligrosidad=peligrosidad
    )
