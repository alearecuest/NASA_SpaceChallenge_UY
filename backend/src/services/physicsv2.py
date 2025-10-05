import math 
from typing import Optional

ASTEROID_PROPERTIES = {
    "stony": {"density": 3000, "strength": 1e7},
    "iron": {"density": 8000, "strength": 1e8},
    "cometary": {"density": 500, "strength": 1e4}
}

TARGET_PROPERTIES = {
    "sedimentary": {"density": 2500, "strength": 5e7, "gravity_correction": 1.2},
    "crystalline": {"density": 2700, "strength": 1e8, "gravity_correction": 1.0},
    "water_deep": {"density:": 1000, "strength": 0, "gravity_correction": 0.8},
    "water_shallow": {"density": 1000, "strength": 0, "gravity_correction": 0.9}
}

# Constantes fisicas
G = 6.67430e-11
EARTH_MASS = 5.972e24 # kg
EARTH_RADIUS = 6371000 # m
ATMOSPHERE_HEIGHT = 100000 # m
AIR_DENSITY_SEA_LEVEL = 1.225
DRAG_COEFFICIENT = 1.0
LUMINOUS_EFFICIENCY = 0.05

def calculate_atmospheric_entry(diameter: float, asteroid_type: str, velocity: float, angle_rad: float) -> dict:
    """
    Simulamos los calculos de un asteroide entrando en la atmosfera
    """

    props = ASTEROID_PROPERTIES[asteroid_type]
    density = props["density"]
    strength = props["strength"]

    radius = diameter / 2
    mass = (4/3) * math.pi * (radius ** 3) * density
    area = math.pi * (radius ** 2)

    v_vertical = velocity * math.sin(angle_rad)

    H = 8000
    rho_breakup = 2 * strength / (velocity ** 2)
    if rho_breakup < AIR_DENSITY_SEA_LEVEL:
        altitude_breakup = -H * math.log(rho_breakup / AIR_DENSITY_SEA_LEVEL)
    else:
        altitude_breakup = 0

    if 0 < altitude_breakup < ATMOSPHERE_HEIGHT:
        energy_joules = 0.5 * mass * (velocity ** 2)
        return {
            "is_airbust": True,
            "altitude_km": altitude_breakup / 1000,
            "energy_joules": energy_joules,
            "final_velocity_km_s": 0
        }
    
    avg_air_density = AIR_DENSITY_SEA_LEVEL / 2
    deceleration_work = 0.5 * DRAG_COEFFICIENT * area * avg_air_density * (velocity ** 2) * ATMOSPHERE_HEIGHT

    initial_ke = 0.5 * mass * (velocity ** 2)
    final_ke = max(0, initial_ke - deceleration_work)

    final_velocity = math.sqrt(2 * final_ke / mass) if final_ke > 0 else 0

    return {
        "is_airbust": False,
        "altitude_km": None,
        "energy_joules": final_ke,
        "final_velocity_km_s": final_velocity / 1000
    }

def calculate_crater_and_ejecta(energy_joules: float, final_velocity: float, target_type: str, angle_rad: float) -> dict:
    """
    Calcular las dimensiones del crater y el volumen de material de ejeccion
    """

    if final_velocity == 0:
        return {"crater_diameter_m": 0, "eject_volume_km3": 0}
    
    target = TARGET_PROPERTIES[target_type]

    gravity = G * EARTH_MASS / (EARTH_RADIUS**2)
    crater_diameter_m = 1.5 * (energy_joules ** 0.25) * (gravity ** -0.25) * target["gravity_correction"]

    effective_diameter = crater_diameter_m / math.sqrt(math.sin(angle_rad))

    crater_depth_m = effective_diameter / 5
    eject_volume_m3 = (1/2) * math.pi * (effective_diameter / 2) ** 2 * crater_depth_m

    return {
        "crater_diameter_m": effective_diameter,
        "eject_volume_km3": eject_volume_m3 / 1e9
    }

def calculate_tsunami(energy_joules: float, water_depth_m: float) -> dict:
    """
    Calcular la altura inicial del tsunami y su altura al llegar a la costa
    """

    if water_depth_m is None or water_depth_m == 0:
        return {"tsunami_initial_height": 0, "tsunami_coastal_height_m": 0}
    
    initial_hieght_m = 0.01 * (energy_joules**0.25) / (water_depth_m**0.5)

    coastal_height_m = initial_hieght_m * 10 

    return {
        "tsunami_initial_height": initial_hieght_m,
        "tsunami_coastal_height": coastal_height_m
    }

def calculate_damage_zones(energy_joules: float, diameter_m: float, is_airbust: bool, airbust_altitude_km: Optional[float]) -> list:
    """
    Calcular las zonas de daños
    """
    zones = []

    burn_radius_m = math.sqrt((LUMINOUS_EFFICIENCY * energy_joules) / (4 * math.pi * 10 * 41840))
    zones.append({
        "radius_km": burn_radius_m / 1000,
        "description": "Quemaduras graves por radiacion termica",
        "overpressure_atm": None,
        "thermal_flux_cal_cm2": 10
    })

    if is_airbust:
        k_shock = 0.3 * (airbust_altitude_km**0.1)
    else:
        k_shock = 0.2

    shock_radius_m = k_shock * (energy_joules**(1/3))
    zones.append({
        "radius_km": shock_radius_m / 1000,
        "description": "Daño estructural severo por onda de choque (sobrepresión > 1 atm)",
        "overpressure_atm": 1.0,
        "thermal_flux_cal_cm2": None
    })

    destruction_radius_m = (diameter_m * 2) if not is_airbust else (diameter_m * 3)
    zones.append({
        "radius_km": destruction_radius_m / 1000,
        "description": "Aniquilación total / eyección de material",
        "overpressure_atm": 20.0,
        "thermal_flux_cal_cm2": None
    })

    zones.sort(key=lambda x: x['radius_km'])
    return zones

def calculate_impact_v2(params: dict) -> dict: 
    """
    Funcion principal que orquesta los calculos del motor de fisica v2
    """

    entry_results = calculate_atmospheric_entry(params["diameter_m"], params["asteroid_type"], params["velocity_km_s"] * 1000, math.radians(params["angle_degrees"]))
    results = {
        "final_velocity_km_s": entry_results["final_velocity_km_s"],
        "is_airbust": entry_results["is_airbust"],
        "airbust_altitude_km": entry_results["altitude_km"],
        "earthquake_magnitude": (2/3) * math.log10(entry_results["energy_joules"] + 1) - 6.0
    }

    if not entry_results["is_airbust"]:
        crater_results = calculate_crater_and_ejecta(
            entry_results["energy_joules"],
            entry_results["final_velocity_km_s"] * 1000,
            params["target_type"],
            math.radians(params["angle_degrees"])
        )
        results.update(crater_results)
    else:
        results["crater_diameter_m"] = 0
        results["eject_volume_km3"] = 0

    if "water" in params["target_type"]:
        tsunami_results = calculate_tsunami(entry_results["energy_joules"], params.get("water_depth_m"))
        results.update(tsunami_results)
    else:
        results["tsunami_initial_height_m"] = 0
        results["tsunami_coastal_height_m"] = 0

    results["damage_zones"] = calculate_damage_zones(
        entry_results["energy_joules"],
        params["diameter_m"],
        entry_results["is_airbust"],
        entry_results["altitude_km"]
    )

    return results