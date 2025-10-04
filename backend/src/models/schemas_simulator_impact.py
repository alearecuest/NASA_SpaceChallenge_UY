from pydantic import BaseModel, Field
from typing import List, Dict, Any

class ImpactInput(BaseModel):
    diameter_m: float =  Field(..., gt=0, description="Diametro del asteroide en metros.")
    density_kg_m3: float = Field(..., gt=0, description="Densidad del asteroide en kg/m3.")
    velocity_km_s: float = Field(..., gt=0, description="Velocidad del asteroide en km/s.")
    angle_degrees: float = Field(..., gt=0, le=90, description="Angulo de impacto en grados.")
    is_water_impact: bool = Field(False, description="True si el impacto es en el oceano, False si el impacto es en la tierra.")

class DamageZone(BaseModel):
    radius_km: float = Field(..., description="Radio de la zona de daño en kilometros.")
    description: str = Field(..., description="Descripcion de los niveles de daño en la zona del impacto.")

class SimulationResult(BaseModel):
    crater_diameter_m: float = Field(..., description="Diamtro estimado del crater tras el impacto del asteroide en metros.")
    fireball_diameter_m: float = Field(..., description="Diametro de la bola de fuego generada por el impacto en metros.")
    shockwave_radius_km: float = Field(..., description="Onda de choque generada por el impacto en kilometros.")
    max_wind_speed_km_h: float = Field(..., description="Velocidad maxima de los vientos por el impacto en km/h.")
    earthquake_magnitude: float = Field(..., description="Magnitud de terremoto generado.")
    tsunami_initial_height_m: float = Field(0, description="Altura inicial de la ola de tsunami en metros (valor por defecto 0 por si el impacto es en la tierra).")
    tsunami_coastal_height_m: float = Field(0, description="Altura estimada de la ola al llegar a la costa en metros (valor por defecto 0 por si el impacto es en la tierra).")
    damage_zones: List[DamageZone] = Field(description="Lista de zonas de afectacion ordenadas por radio.")