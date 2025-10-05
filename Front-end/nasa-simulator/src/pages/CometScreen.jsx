import { useNavigate } from 'react-router-dom';
import { cometList } from '../data/cometData';
import '../styles/AsteroidScreen.css';

function CometScreen() {
  const navigate = useNavigate();

  const getDangerClass = (danger) => {
    switch(danger.toLowerCase()) {
      case 'low': return 'danger-low';
      case 'medium': return 'danger-medium';
      case 'high': return 'danger-high';
      default: return 'danger-low';
    }
  };

  return (
    <main className="frame" aria-label="Comet list">
      <div className="corner" aria-hidden="true"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">Comets</h1>
        </div>
        <button className="btn" onClick={() => navigate('/')}>
          ← Back to Home
        </button>
      </div>

      <div className="table-container">
        <table>
          <thead>
            <tr>
              <th>Name</th>
              <th>Size (km)</th>
              <th>Composition</th>
              <th>Danger Scale</th>
            </tr>
          </thead>
          <tbody>
            {cometList.map((comet) => (
              <tr 
                key={comet.id} 
                onClick={() => navigate(`/comets/${comet.id}`)}
                style={{ cursor: 'pointer' }}
              >
                <td>{comet.name}</td>
                <td>{comet.size}</td>
                <td>{comet.composition.split(',')[0].trim()}</td>
                <td>
                  <span className={getDangerClass(comet.danger)}>
                    {comet.danger}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  );
}

export default CometScreen;
