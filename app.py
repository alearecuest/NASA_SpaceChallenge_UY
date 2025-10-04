from fastapi import FastAPI
from simulator.models import ImpactInput, SimulationResult
from simulator.pyshics import calculate_impact

app = FastAPI(
    title="Asteroid Impact Simulation API", 
    description="API para simular los efectos de un impacto de asteroide", 
    version="0.0.1"
    )

@app.post("/simulate", response_model=SimulationResult)
async def simulate_impact(input_data: ImpactInput):
    """
    Recibe los parametros del asteroide y devuelve los resultados de la simulacion.
    """

    results = calculate_impact(
        diameter=input_data.diameter_m,
        density=input_data.density_kg_m3,
        velocity=input_data.velocity_km_s
        )
    
    return SimulationResult(**results)