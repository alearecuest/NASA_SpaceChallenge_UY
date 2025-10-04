# models.py

from pydantic import BaseModel, Field
from typing import Optional, List

# --- Modelo para la respuesta final de nuestra API (sin cambios) ---
class NeoData(BaseModel):
    nombre: str = Field(..., description="Nombre del asteroide.")
    designacion: str = Field(..., description="Designación única de la NASA.")
    diametro_min_m: float = Field(..., description="Diámetro mínimo estimado en metros.")
    diametro_max_m: float = Field(..., description="Diámetro máximo estimado en metros.")
    distancia_actual_km: Optional[float] = Field(None, description="Distancia de la aproximación más cercana a la Tierra en kilómetros.")
    velocidad_relativa_km_s: Optional[float] = Field(None, description="Velocidad en la aproximación más cercana a la Tierra (km/s).")
    riesgo_torino: int = Field(..., description="Escala de riesgo de Torino (simplificado).")
    riesgo_palermo: float = Field(..., description="Escala de riesgo de Palermo (simplificado).")
    composicion_estimada: str = Field(..., description="Composición estimada.")
    energia_impacto_joules: Optional[float] = Field(None, description="Energía cinética de impacto en Julios (calculada).")
    peligrosidad: str = Field(..., description="Descripción simple del nivel de peligro.")

# --- Modelos para parsear la respuesta de la API NeoWS de la NASA ---
class EstimatedDiameter(BaseModel):
    meters: dict

class RelativeVelocity(BaseModel):
    kilometers_per_second: str

class MissDistance(BaseModel):
    kilometers: str
    astronomical: str
    lunar: str

class CloseApproachData(BaseModel):
    close_approach_date: str
    orbiting_body: str
    relative_velocity: RelativeVelocity
    miss_distance: MissDistance

class NasaNeoWSResponse(BaseModel):
    id: str
    name: str
    designation: str
    is_potentially_hazardous_asteroid: bool
    estimated_diameter: EstimatedDiameter
    close_approach_data: List[CloseApproachData]