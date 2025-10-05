import { useNavigate } from 'react-router-dom';
import { asteroidList } from '../data/asteroidData';
import '../styles/AsteroidScreen.css';

function AsteroidScreen() {
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
    <main className="frame" aria-label="Asteroid list">
      <div className="corner" aria-hidden="true"></div>
      
      <div className="header">
        <div className="brand">
          <h1 className="title">Asteroids</h1>
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
            {asteroidList.map((asteroid) => (
              <tr 
                key={asteroid.id} 
                onClick={() => navigate(`/asteroids/${asteroid.id}`)}
                style={{ cursor: 'pointer' }}
              >
                <td>{asteroid.name}</td>
                <td>{asteroid.size}</td>
                <td>{asteroid.composition.split('(')[0].trim()}</td>
                <td>
                  <span className={getDangerClass(asteroid.danger)}>
                    {asteroid.danger}
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

export default AsteroidScreen;
