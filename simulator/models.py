from pydantic import BaseModel

class ImpactInput(BaseModel):
    diameter_m: float
    density_kg_m3: float
    velocity_km_s: float
    angle_degrees: float
    is_water_impact: bool = False

class SimulationResult(BaseModel):
    crater_diameter_m: float
    fireball_diameter_m: float
    shockwave_radius_km: float
    max_wind_speed_km_h: float
    earthquake_magnitude: float
