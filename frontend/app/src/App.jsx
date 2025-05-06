import React from 'react';

import PlotMap from "./components/mapa.jsx";
import PlotPie from "./components/endereco.jsx";
import PlotBar from "./components/curso.jsx";
import PlotGenderBar from "./components/genero.jsx";
import PlotIndicator from "./components/transport.jsx"

import Sideba from "./components/sidebar/index.jsx"
import './App.css';

function App() {
  return (
    <div className="MapDiv">
        <Sideba/>


    <div className='Graficos'>
      <div>
      	<PlotIndicator/>
      </div>

      <div>
        <PlotGenderBar/>
      </div>

      <div>
            <PlotPie/>
      </div>

      <div>
        <PlotMap/>
      </div>

      <div>
        <PlotBar/>
      </div>
    </div>

    </div>
  );
}

export default App;
