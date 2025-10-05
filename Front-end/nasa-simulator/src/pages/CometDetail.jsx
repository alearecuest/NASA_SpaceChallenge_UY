import { useParams, useNavigate } from 'react-router-dom';
import { cometData } from '../data/cometData';
import '../styles/DetailScreen.css';

function CometDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const comet = cometData[id];

  if (!comet) {
    return (
      <main className="frame">
        <div className="corner" aria-hidden="true"></div>
        <h2>Comet not found</h2>
        <button className="btn" onClick={() => navigate('/comets')}>
          ← Back to List
        </button>
      </main>
    );
  }

  const fields = [
    { label: 'Size', value: comet.size },
    { label: 'Composition', value: comet.composition },
    { label: 'Danger Level', value: comet.danger },
    { label: 'Orbital Period', value: comet.orbit },
    { label: 'Distance from Sun', value: comet.distance },
    { label: 'Discovered', value: comet.discovered },
    { label: 'Discoverer', value: comet.discoverer },
    { label: 'Mass', value: comet.mass },
    { label: 'Density', value: comet.density },
    { label: 'Rotation Period', value: comet.rotation },
    { label: 'Perihelion', value: comet.perihelion }
  ];

  return (
    <main className="frame" aria-label="Comet details">
      <div className="corner" aria-hidden="true"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">{comet.name}</h1>
        </div>
        <button className="btn" onClick={() => navigate('/comets')}>
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

      {comet.notes && (
        <div className="notes">
          <h3>Additional Notes</h3>
          <p>{comet.notes}</p>
        </div>
      )}

      <div className="simulation-button-container">
        <button 
          className="btn-simulation" 
          onClick={() => navigate(`/simulation/comet/${id}`)}
        >
          🌍 Simulation
        </button>
      </div>
    </main>
  );
}

export default CometDetail;
