import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainScreen from './pages/MainScreen';
import AsteroidScreen from './pages/AsteroidScreen';
import AsteroidDetail from './pages/AsteroidDetail';
import CometScreen from './pages/CometScreen';
import CometDetail from './pages/CometDetail';
import Simulation from './pages/Simulation';
import './styles/global.css';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainScreen />} />
        <Route path="/asteroids" element={<AsteroidScreen />} />
        <Route path="/asteroids/:id" element={<AsteroidDetail />} />
        <Route path="/comets" element={<CometScreen />} />
        <Route path="/comets/:id" element={<CometDetail />} />
        <Route path="/simulation/:type/:id" element={<Simulation />} />
      </Routes>
    </Router>
  );
}

export default App;
