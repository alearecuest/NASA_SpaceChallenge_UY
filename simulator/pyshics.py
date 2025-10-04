import math

# Constantes de calibracion (es para probar y jugar con ellas)

K_CRATER = 0.12
K_FIREBALL = 0.0015
K_SHOCKWAVE = 0.0008
K_WIND = 150


def calculate_impact(diameter: float, density: float, velocity: float) -> dict:
    """
    Funcion que contiene la logica matematica del impacto
    """

    radius_m = diameter / 2
    volume_m3 = (4/3) * math.pi * (radius_m ** 3)
    mass_kg = volume_m3 * density
    velocity_m_s = velocity * 1000
    energy_joules = 0.5 * mass_kg * (velocity_m_s ** 2)

    result = {}

    result['earthquake_magnitude'] = (2/3) * math.log10(energy_joules) - 6.06

    result['crater_diameter_m'] = K_CRATER * (energy_joules ** (1/3.4))

    result['fireball_diameter_m'] = K_FIREBALL * (energy_joules ** (1/3))

    result['shockwave_radius_km'] = (K_SHOCKWAVE * (energy_joules ** 0.4)) / 1000

    result['max_wind_speed_km_h'] = K_WIND * (energy_joules ** 0.25)

    return result
