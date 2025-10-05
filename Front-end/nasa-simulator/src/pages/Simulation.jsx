import { useParams, useNavigate } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { asteroidData } from '../data/asteroidData';
import { cometData } from '../data/cometData';
import '../styles/Simulation.css';

function Simulation() {
  const { type, id } = useParams();
  const navigate = useNavigate();
  const [impactLocation, setImpactLocation] = useState(null);
  
  const data = type === 'asteroid' ? asteroidData[id] : cometData[id];

  useEffect(() => {
    const randomLat = (Math.random() * 180 - 90).toFixed(4);
    const randomLng = (Math.random() * 360 - 180).toFixed(4);
    setImpactLocation({ lat: randomLat, lng: randomLng });
  }, []);

  const handleBackToList = () => {
    if (type === 'asteroid') {
      navigate('/asteroids');
    } else {
      navigate('/comets');
    }
  };

  if (!data) {
    return (
      <main className="frame">
        <div className="corner"></div>
        <h2>Object not found</h2>
        <button className="btn" onClick={handleBackToList}>
          Back to List
        </button>
      </main>
    );
  }

  const getImpactRadius = () => {
    const size = parseFloat(data.size);
    return (size * 10).toFixed(1);
  };

  const getImpactEnergy = () => {
    const size = parseFloat(data.size);
    const energy = Math.pow(size, 3) * 1000;
    return energy.toFixed(2);
  };

  return (
    <main className="frame simulation-frame">
      <div className="corner"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">Impact Simulation</h1>
          <p className="subtitle-small">{data.name}</p>
        </div>
        <button className="btn" onClick={handleBackToList}>
          ← Back to List
        </button>
      </div>

      <div className="simulation-container">
        <div className="simulation-map">
          <iframe
            title="Earth Map"
            src={`https://www.openstreetmap.org/export/embed.html?bbox=-180,-90,180,90&layer=mapnik&marker=${impactLocation?.lat},${impactLocation?.lng}`}
            style={{
              width: '100%',
              height: '100%',
              border: 'none',
              borderRadius: '12px'
            }}
          />
          <div className="impact-marker">
            <div className="impact-point"></div>
            <div className="impact-ripple"></div>
          </div>
        </div>

        <div className="simulation-info">
          <h2>Impact Data</h2>
          
          <div className="info-grid">
            <div className="info-card">
              <div className="info-label">Impact Location</div>
              <div className="info-value">
                {impactLocation ? `${impactLocation.lat}°, ${impactLocation.lng}°` : 'Calculating...'}
              </div>
            </div>

            <div className="info-card">
              <div className="info-label">Impact Radius</div>
              <div className="info-value">{getImpactRadius()} km</div>
            </div>

            <div className="info-card">
              <div className="info-label">Estimated Energy</div>
              <div className="info-value">{getImpactEnergy()} MT</div>
            </div>

            <div className="info-card">
              <div className="info-label">Danger Level</div>
              <div className={`info-value danger-${data.danger.toLowerCase()}`}>
                {data.danger}
              </div>
            </div>

            <div className="info-card">
              <div className="info-label">Object Size</div>
              <div className="info-value">{data.size}</div>
            </div>

            <div className="info-card">
              <div className="info-label">Composition</div>
              <div className="info-value">{data.composition.split('(')[0].trim()}</div>
            </div>
          </div>

          <div className="warning-box">
            <h3>⚠️ Impact Effects</h3>
            <ul>
              <li>Crater diameter: ~{(getImpactRadius() * 2).toFixed(1)} km</li>
              <li>Seismic activity: Magnitude {(parseFloat(data.size) * 2).toFixed(1)}</li>
              <li>Thermal radiation radius: {(getImpactRadius() * 3).toFixed(1)} km</li>
              <li>Shock wave propagation: Global atmospheric disturbance</li>
            </ul>
          </div>
        </div>
      </div>
    </main>
  );
}

export default Simulation;
