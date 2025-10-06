# NEO Simulator

A modern web application for exploring and simulating asteroid and comet impacts on Earth. Built with React and featuring real astronomical data visualization.

## Features

- **Interactive Object Catalog**: Browse through a comprehensive list of asteroids and comets
- **Detailed Information**: View complete data about each celestial object including:
  - Size, composition, and mass
  - Orbital characteristics
  - Discovery information
  - Danger level assessment
- **Impact Simulation**: Visualize potential impact scenarios with:
  - Interactive map showing impact location
  - Calculated impact radius and energy
  - Estimated damage effects
  - Seismic and thermal radiation projections
- **Responsive Design**: Fully optimized for desktop, tablet, and mobile devices
- **Modern UI/UX**: Sleek space-themed interface with smooth animations

## Technologies Used

- **Frontend Framework**: React 18.x
- **Routing**: React Router DOM v6
- **Styling**: Custom CSS with modern design patterns
- **Maps**: OpenStreetMap integration
- **Build Tool**: Create React App
- **Package Manager**: npm

## Pre requisites

Before you begin, ensure you have the following installed:

- **Node.js** 
- **npm**
- **fastapi**
- **uvicorn**
- **httpx**
- **pydantic**
- **pydantic-settings**
- **python-dotenv**

### Installing Node.js and npm on Ubuntu/Debian:

```bash
# Quick install
sudo apt update
sudo apt install nodejs npm

# Verify installation
node --version
npm --version
```

## Installation

1. **Clone the repository**

```bash
git clone https://github.com/alearecuest/NASA_SpaceChallenge_UY.git
```

2. **Install dependencies**

```bash
npm install
```

3. **Start the development server**

```bash
npm start
```

4. **Open your browser**

Navigate to [http://localhost:3000](http://localhost:3000)

## Project Structure

```
nasa-simulator/
├── public/
│   └── index.html
├── src/
│   ├── data/
│   │   ├── asteroidData.js
│   │   └── cometData.js
│   ├── pages/
│   │   ├── MainScreen.jsx
│   │   ├── AsteroidScreen.jsx
│   │   ├── AsteroidDetail.jsx
│   │   ├── CometScreen.jsx
│   │   ├── CometDetail.jsx
│   │   └── Simulation.jsx
│   ├── styles/
│   │   ├── global.css 
│   │   ├── MainScreen.css
│   │   ├── AsteroidScreen.css
│   │   ├── DetailScreen.css
│   │   └── Simulation.css
│   ├── App.jsx
│   └── index.js
├── package.json
└── README.md
```

## Usage

### Browsing Objects

1. From the main screen, click **"Asteroid"** or **"Comet"**
2. Browse through the list of objects
3. Click on any row to view detailed information

### Running Simulations

1. Navigate to any asteroid or comet detail page
2. Click the **"Simulation"** button
3. View the impact location on the interactive map
4. Review calculated impact data and effects

### Navigation

- **Back to Home**: Click the logo or use the back button
- **Back to List**: Return to the object catalog from detail pages
- **Browse Objects**: Click on table rows to navigate between objects

## Available Scripts

### `npm start`

Runs the app in development mode.  
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

### `npm run build`

Builds the app for production to the `build` folder.  
The build is minified and optimized for best performance.

## Backend Integration

The application is being prepared to connect with a backend API for:

- Real-time astronomical data
- User simulation history
- Advanced impact calculations
- Database storage for custom scenarios

Backend endpoints (in development):
- `GET /api/asteroids` - Fetch all asteroids
- `GET /api/asteroids/:id` - Get asteroid by ID
- `GET /api/comets` - Fetch all comets
- `GET /api/comets/:id` - Get comet by ID
- `POST /api/simulation` - Create impact simulation

## Design Features

- **Space Theme**: Dark gradient backgrounds with cosmic vibes
- **Glassmorphism**: Modern frosted glass effects
- **Smooth Animations**: Transitions and hover effects
- **Custom Fonts**: Audiowide for headers, Outfit for body text
- **Color Palette**:
  - Primary: `#b7a5ff` (Lavender)
  - Secondary: `#cfbfff` (Light Purple)
  - Danger High: `#ff6b6b` (Red)
  - Danger Medium: `#ffd97d` (Yellow)
  - Danger Low: `#7cffb2` (Green)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## Authors

**Aylin Pintos, Luna Leguizamo, Jorge Beritan, Alejandro Arévalo** 


