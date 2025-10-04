from fastapi import FastAPI
from models.schemas_simulator_impact import SimulationResult, ImpactInput
from services.physics import calculate_impact
from api.routes import main_router

app = FastAPI(
    title="NASA Asteroids API",
    description="API para obtener datos de asteroides de la NASA",
    version="1.0.0"
)

# Incluir todas las rutas
app.include_router(main_router)

@app.get("/")
async def root():
    return {"message": "NASA Asteroids API running!"}

@app.post("/simulate", response_model=SimulationResult)
async def simulate_impact(input_data: ImpactInput):
    """
    Recibe los datos para la simulacion
    """
    results = calculate_impact(
        diameter=input_data.diameter_m,
        density=input_data.density_kg_m3,
        velocity=input_data.velocity_km_s,
        is_water_impact=input_data.is_water_impact
    )

    return SimulationResult(**results)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)