import { useParams, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import '../styles/Simulation.css';

function Simulation() {
  const { type, id } = useParams();
  const navigate = useNavigate();

  // --- Estados para la gestión de datos y UI ---
  const [asteroidData, setAsteroidData] = useState(null);
  const [simulationData, setSimulationData] = useState(null);
  const [impactLocation, setImpactLocation] = useState(null);
  
  const [isLoading, setIsLoading] = useState(true); // Cargando datos del asteroide
  const [isSimulating, setIsSimulating] = useState(false); // Cargando simulación
  const [error, setError] = useState(null); // Error al obtener el asteroide
  const [simulationError, setSimulationError] = useState(null); // Error en la simulación

  // --- Estados para los parámetros de la simulación ---
  const [impactAngle, setImpactAngle] = useState(45); // Ángulo por defecto
  const [isWaterImpact, setIsWaterImpact] = useState(false); // Por defecto, impacto en tierra

  // --- Efecto para obtener los datos del asteroide ---
  useEffect(() => {
    const fetchAsteroidData = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const response = await fetch(`http://localhost:8000/neo/${id}`);
        if (!response.ok) {
          throw new Error(`Error al obtener datos del asteroide: ${response.statusText}`);
        }
        const data = await response.json();
        setAsteroidData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    if (type === 'asteroid' && id) {
      fetchAsteroidData();
    } else {
      // Manejar el caso de cometas o si no hay ID
      setError("Tipo de objeto no soportado o ID no proporcionado.");
      setIsLoading(false);
    }
  }, [type, id]);

  // --- Efecto para ejecutar la simulación cuando los datos del asteroide o los parámetros cambian ---
  useEffect(() => {
    if (asteroidData) {
      runSimulation();
    }
  }, [asteroidData, impactAngle, isWaterImpact]); // Se vuelve a ejecutar si estos parámetros cambian

  // --- Efecto para generar una ubicación de impacto aleatoria ---
  useEffect(() => {
    const randomLat = (Math.random() * 180 - 90).toFixed(4);
    const randomLng = (Math.random() * 360 - 180).toFixed(4);
    setImpactLocation({ lat: randomLat, lng: randomLng });
  }, []);

  // --- Función para llamar al endpoint de simulación ---
  const runSimulation = async () => {
    setIsSimulating(true);
    setSimulationError(null);
    
    // Usamos la misma densidad por defecto que en tu backend
    const DEFAULT_DENSITY = 2500; 

    const payload = {
      diameter_m: asteroidData.size,
      density_kg_m3: DEFAULT_DENSITY,
      velocity_km_s: asteroidData.velocidad_relativa_km_s,
      angle_degrees: impactAngle,
      is_water_impact: isWaterImpact,
    };

    try {
      const response = await fetch('http://localhost:8000/simulate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (!response.ok) {
        throw new Error(`Error en la simulación: ${response.statusText}`);
      }

      const result = await response.json();
      setSimulationData(result);
    } catch (err) {
      setSimulationError(err.message);
    } finally {
      setIsSimulating(false);
    }
  };

  const handleBackToList = () => {
    navigate('/asteroids');
  };

  // --- Renderizado Condicional ---

  if (isLoading) {
    return (
      <main className="frame">
        <div className="corner"></div>
        <h2>Cargando datos del asteroide...</h2>
      </main>
    );
  }

  if (error) {
    return (
      <main className="frame">
        <div className="corner"></div>
        <h2>Error</h2>
        <p>{error}</p>
        <button className="btn" onClick={handleBackToList}>
          ← Volver a la lista
        </button>
      </main>
    );
  }

  if (!asteroidData) {
    return (
      <main className="frame">
        <div className="corner"></div>
        <h2>Objeto no encontrado</h2>
        <button className="btn" onClick={handleBackToList}>
          Volver a la lista
        </button>
      </main>
    );
  }

  // --- Renderizado principal cuando los datos están listos ---
  return (
    <main className="frame simulation-frame">
      <div className="corner"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">Simulación de Impacto</h1>
          <p className="subtitle-small">{asteroidData.nombre}</p>
        </div>
        <button className="btn" onClick={handleBackToList}>
          ← Volver a la lista
        </button>
      </div>

      {/* --- Controles de Simulación --- */}
      <div className="simulation-controls">
        <div className="control-group">
          <label htmlFor="angle-slider">Ángulo de Impacto: {impactAngle}°</label>
          <input
            id="angle-slider"
            type="range"
            min="1"
            max="90"
            value={impactAngle}
            onChange={(e) => setImpactAngle(Number(e.target.value))}
          />
        </div>
        <div className="control-group">
          <label>
            <input
              type="checkbox"
              checked={isWaterImpact}
              onChange={(e) => setIsWaterImpact(e.target.checked)}
            />
            Impacto en Océano
          </label>
        </div>
      </div>

      <div className="simulation-container">
        <div className="simulation-map">
          <iframe
            title="Earth Map"
            src={`https://www.openstreetmap.org/export/embed.html?bbox=-180,-90,180,90&layer=mapnik&marker=${impactLocation?.lat},${impactLocation?.lng}`}
            style={{ width: '100%', height: '100%', border: 'none', borderRadius: '12px' }}
          />
          <div className="impact-marker">
            <div className="impact-point"></div>
            <div className="impact-ripple"></div>
          </div>
        </div>

        <div className="simulation-info">
          <h2>Datos del Impacto</h2>
          
          {isSimulating && <p>Ejecutando simulación...</p>}
          {simulationError && <p className="error-message">Error en la simulación: {simulationError}</p>}

          {simulationData && (
            <div className="info-grid">
              <div className="info-card">
                <div className="info-label">Diámetro del Cráter</div>
                <div className="info-value">{(simulationData.crater_diameter_m / 1000).toFixed(2)} km</div>
              </div>

              {!isWaterImpact && (
                <>
                  <div className="info-card">
                    <div className="info-label">Diámetro de Bola de Fuego</div>
                    <div className="info-value">{(simulationData.fireball_diameter_m / 1000).toFixed(2)} km</div>
                  </div>
                  <div className="info-card">
                    <div className="info-label">Radio de Onda de Choque</div>
                    <div className="info-value">{simulationData.shockwave_radius_km.toFixed(2)} km</div>
                  </div>
                </>
              )}

              {isWaterImpact && (
                <>
                  <div className="info-card">
                    <div className="info-label">Altura Inicial de Tsunami</div>
                    <div className="info-value">{simulationData.tsunami_initial_height_m.toFixed(2)} m</div>
                  </div>
                  <div className="info-card">
                    <div className="info-label">Altura en Costa</div>
                    <div className="info-value">{simulationData.tsunami_coastal_height_m.toFixed(2)} m</div>
                  </div>
                </>
              )}

              <div className="info-card">
                <div className="info-label">Magnitud de Terremoto</div>
                <div className="info-value">{simulationData.earthquake_magnitude.toFixed(1)}</div>
              </div>
              
              <div className="info-card">
                <div className="info-label">Velocidad Máxima del Viento</div>
                <div className="info-value">{simulationData.max_wind_speed_km_h.toFixed(0)} km/h</div>
              </div>
            </div>
          )}

          {simulationData && simulationData.damage_zones && (
            <div className="warning-box">
              <h3>⚠️ Zonas de Afectación</h3>
              <ul>
                {simulationData.damage_zones.map((zone, index) => (
                  <li key={index}>
                    <strong>{zone.description}:</strong> Radio de {zone.radius_km.toFixed(2)} km
                  </li>
                ))}
              </ul>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}

export default Simulation;