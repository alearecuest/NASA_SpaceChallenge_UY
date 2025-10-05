import { useParams, useNavigate } from 'react-router-dom';
import { asteroidData } from '../data/asteroidData';
import '../styles/DetailScreen.css';

function AsteroidDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const asteroid = asteroidData[id];

  if (!asteroid) {
    return (
      <main className="frame">
        <div className="corner" aria-hidden="true"></div>
        <h2>Asteroid not found</h2>
        <button className="btn" onClick={() => navigate('/asteroids')}>
          ← Back to List
        </button>
      </main>
    );
  }

  const fields = [
    { label: 'Size', value: asteroid.size },
    { label: 'Composition', value: asteroid.composition },
    { label: 'Danger Level', value: asteroid.danger },
    { label: 'Orbital Period', value: asteroid.orbit },
    { label: 'Distance from Sun', value: asteroid.distance },
    { label: 'Discovered', value: asteroid.discovered },
    { label: 'Discoverer', value: asteroid.discoverer },
    { label: 'Mass', value: asteroid.mass },
    { label: 'Density', value: asteroid.density },
    { label: 'Rotation Period', value: asteroid.rotation },
    { label: 'Surface Temperature', value: asteroid.surface_temp }
  ];

  return (
    <main className="frame" aria-label="Asteroid details">
      <div className="corner" aria-hidden="true"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">{asteroid.name}</h1>
        </div>
        <button className="btn" onClick={() => navigate('/asteroids')}>
          ← Back to List
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

      {asteroid.notes && (
        <div className="notes">
          <h3>Additional Notes</h3>
          <p>{asteroid.notes}</p>
        </div>
      )}

      <div className="simulation-button-container">
        <button 
          className="btn-simulation" 
          onClick={() => navigate(`/simulation/asteroid/${id}`)}
        >
          🌍 Simulation
        </button>
      </div>
    </main>
  );
}

export default AsteroidDetail;
