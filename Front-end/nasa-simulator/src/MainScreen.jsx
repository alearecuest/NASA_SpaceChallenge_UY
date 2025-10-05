import { useNavigate } from 'react-router-dom';
import '../styles/MainScreen.css';

function MainScreen() {
  const navigate = useNavigate();

  return (
    <main className="frame" aria-label="NASA Simulator landing">
      <div className="corner" aria-hidden="true"></div>
      <section className="grid">
        <div className="brand">
          <h1 className="title">NASA</h1>
          <h2 className="subtitle">Simulator</h2>
          <div className="cta">
            <button 
              className="btn" 
              onClick={() => navigate('/asteroids')}
              aria-label="Open asteroid list"
            >
              Asteroid
            </button>
            <button 
              className="btn secondary" 
              onClick={() => navigate('/comets')}
              aria-label="Open comet list"
            >
              Comet
            </button>
          </div>
        </div>

        <div className="planet-wrap">
          <img 
            className="earth" 
            alt="Earth view" 
            src="https://upload.wikimedia.org/wikipedia/commons/9/97/The_Earth_seen_from_Apollo_17.jpg" 
          />
        </div>
      </section>
    </main>
  );
}

export default MainScreen;
