import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import '../styles/DetailScreen.css';


function AsteroidDetail() {
  const { id } = useParams();
  const navigate = useNavigate();

  const [asteroid, setAsteroid] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchAsteroidData = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const response = await fetch(`http://localhost:8000/neo/${id}`);
        
        if (!response.ok) {
          throw new Error(`Error al obtener los datos: ${response.statusText} (Código: ${response.status})`);
        }
        
        const data = await response.json();
        setAsteroid(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    if (id) {
      fetchAsteroidData();
    }
  }, [id]); 

  if (isLoading) {
    return (
      <main className="frame">
        <div className="corner" aria-hidden="true"></div>
        <h2>Cargando datos del asteroide...</h2>
      </main>
    );
  }


  if (error) {
    return (
      <main className="frame">
        <div className="corner" aria-hidden="true"></div>
        <h2>Error</h2>
        <p>{error}</p>
        <button className="btn" onClick={() => navigate('/asteroids')}>
          ← Volver a la lista
        </button>
      </main>
    );
  }

  if (!asteroid) {
    return (
      <main className="frame">
        <div className="corner" aria-hidden="true"></div>
        <h2>Asteroide no encontrado</h2>
        <button className="btn" onClick={() => navigate('/asteroids')}>
          ← Volver a la lista
        </button>
      </main>
    );
  }

  const fields = [
    { label: 'Name', value: asteroid.nombre },
    { label: 'NASA Designation', value: asteroid.designacion },
    { label: 'Average Diameter (m)', value: asteroid.size ? `${asteroid.size.toFixed(2)} m` : 'No disponible' },
    { label: 'Current Distance (km)', value: asteroid.distancia_actual_km ? `${asteroid.distancia_actual_km.toLocaleString()} km` : 'No disponible' },
    { label: 'Relative Speed (km/s)', value: asteroid.velocidad_relativa_km_s ? `${asteroid.velocidad_relativa_km_s.toFixed(2)} km/s` : 'No disponible' },
    { label: 'Risk Scale (Torine)', value: asteroid.riesgo_torino },
    { label: 'Risk Scale (Palermo)', value: asteroid.riesgo_palermo },
    { label: 'Estimated Composition', value: asteroid.composicion_estimada },
    { label: 'Impact Energy (Jules)', value: asteroid.energia_impacto_joules ? `${asteroid.energia_impacto_joules.toExponential(2)} J` : 'No disponible' },
    { label: 'Level of Danger', value: asteroid.peligrosidad },
  ];

  return (
    <main className="frame" aria-label="Asteroid details">
      <div className="corner" aria-hidden="true"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">{asteroid.nombre}</h1>
        </div>
        <button className="btn" onClick={() => navigate('/asteroids')}>
          ← Volver a la lista
        </button>
      </div>

      <div className="detail-grid">
        {fields.map((field, index) => (
          <div key={index} className="detail-row">
            <div className="detail-label">{field.label}</div>
            <div className="detail-value">{field.value}</div>
          </div>
        ))}
      </div>

      <div className="simulation-button-container">
        <button 
          className="btn-simulation" 
          onClick={() => navigate(`/simulation/asteroid/${id}`)}
        >
          🌍 Simulación
        </button>
      </div>
    </main>
  );
}

export default AsteroidDetail;