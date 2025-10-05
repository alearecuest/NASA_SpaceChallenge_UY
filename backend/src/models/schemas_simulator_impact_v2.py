from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from enum import Enum

class AsteroidType(str, Enum):
    STONY = "stony"
    IRON = "iron"
    COMETARY = "cometary"

class TargetType(str, Enum):
    SEDIMENTARY_ROCK = "sedimentary"
    CRYSTALLINE_ROCK = "crystalline"
    WATER_DEEP = "water_deep"
    WATER_SHALLOW = "water_shallow"

class ImpactInputV2(BaseModel):
    diameter_m: float
    asteroid_type: AsteroidType
    velocity_km_s: float
    angle_degrees: float
    target_type: TargetType
    water_depth_m: Optional[float] = Field(None, ge=0, description="...")

class DamageZoneV2(BaseModel):
    radius_km: float
    description: str
    overpressure_atm: Optional[float]
    thermal_flux_cal_cm2: Optional[float]

class SimulationResultV2(BaseModel):
    final_velocity_km_s: float
    is_airbust: bool
    airbust_altitude_km: Optional[float]
    crater_diameter_m: Optional[float]
    eject_volume_km3: Optional[float]
    earthquake_magnitude: float
    tsunami_initial_height_m: Optional[float]
    tsunami_coastal_height_m: Optional[float]
    damage_zones: List[DamageZoneV2]

