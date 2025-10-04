from fastapi import FastAPI
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)