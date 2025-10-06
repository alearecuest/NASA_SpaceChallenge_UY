import math

# Constantes de calibración (se pueden modificar para testing)
K_CRATER = 0.02
K_FIREBALL = 0.004
K_SHOCKWAVE = 0.002
K_WIND = 0.55
K_TSUNAMI = 0.0005

def calculate_impact(diameter: float, density: float, velocity: float, angle_degrees, is_water_impact: bool) -> dict:
    """
    Funcion principal para orquestar los calculos
    """

    radius_m = diameter / 2
    volume_m3 = (4/3) * math.pi * (radius_m ** 3)
    mass_kg = volume_m3 * density
    velocity_m_s = velocity * 1000
    energy_joules = 0.5 * mass_kg * (velocity_m_s ** 2)
    angle_rad = math.radians(angle_degrees)
    velocity_vertical_m_s = velocity_m_s * math.sin(angle_rad)
    effecive_energy_joules = 0

    results = {}

    if is_water_impact:
        results['crater_diameter_m'] = K_CRATER * (energy_joules ** (1/3.4)) * 0.5

        # Las ondas de choque y la bola de fuego es igual a 0 en estos por el impacto en el agua
        results['fireball_diameter_m'] = 0
        results['shockwave_radius_km'] = 0

        initial_wave_height_m = K_TSUNAMI * (energy_joules ** 0.25)
        results['tsunami_initial_height_m'] = initial_wave_height_m

        results['tsunami_coastal_height_m'] = initial_wave_height_m * 0.8 # Todos estos calculos son estimativos despues se depuran mejor 
    
    else:
        results['crater_diameter_m'] = K_CRATER * (energy_joules ** (1/3.4))
        results['fireball_diameter_m'] = K_FIREBALL * (energy_joules ** (1/3))
        results['shockwave_radius_km'] = (K_SHOCKWAVE * (energy_joules ** 0.4)) / 1000

        results['tsunami_initial_height_m'] = 0
        results['tsunami_coastal_height_m'] = 0

    results['earthquake_magnitude'] = (2/3) * math.log10(energy_joules) - 6.0
    results['max_wind_speed_km_h'] = K_WIND * (energy_joules ** 0.25)

    zones = []

    vaporization_radius = (energy_joules ** 0.2) / 1000
    zones.append({'radius_km': vaporization_radius, "description": "Total evaporation"})

    destruction_radius = (energy_joules ** 0.21) / 1000
    zones.append({"radius_km": destruction_radius, "description": "Total Destruction"})

    severe_damage_radius = (energy_joules ** 0.23) / 1000
    zones.append({"radius_km": severe_damage_radius, "description": "Severe damage, widespread fires"})

    results['damage_zones'] = zones

    return results

