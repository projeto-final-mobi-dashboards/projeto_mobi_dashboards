import React from 'react';
import PlotMap from "./components/map.js";
import PlotPie from "./components/pie.js";
import PlotBar from "./components/bar.js";
import Gender from "./components/gender.js";
import Sideba from "./components/sidebar/index.jsx"
import './App.css';

function App() {
  return (
    <div className="MapDiv">
        <Sideba/>
      <div className='Graficos'>
        <PlotBar/>
        <PlotMap/>
        <PlotPie/>
        <Gender/>
      </div>

    </div>
  );
}

export default App;
