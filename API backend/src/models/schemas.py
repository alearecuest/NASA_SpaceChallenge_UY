from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class CloseApproachData(BaseModel):
    close_approach_date: str
    orbiting_body: str
    relative_velocity: dict
    miss_distance: dict

class Asteroid(BaseModel):
    id: str
    name: str
    estimated_diameter: dict
    is_potentially_hazardous: bool
    close_approach_data: List[CloseApproachData]

class AsteroidFeed(BaseModel):
    element_count: int
    near_earth_objects: dict
