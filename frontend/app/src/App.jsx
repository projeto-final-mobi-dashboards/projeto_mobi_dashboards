import React, { useEffect, useState } from 'react';

import PlotMap from "./components/mapa.jsx";
import PlotPie from "./components/endereco.jsx";
import PlotBar from "./components/curso.jsx";
import PlotGenderBar from "./components/genero.jsx";
import PlotIndicator from "./components/transport.jsx"

import Sideba from "./components/sidebar/index.jsx"
import './App.css';

function App() {
  const [Refresh,setRefresh]=useState('')
  useEffect(
    ()=>{
    const eventSource= new EventSource("/refreshEvent")

    eventSource.onmessage = (event)=> //evento que ocorro ao receber uma mensagem de uma fonte de evento
    {
    	const data = JSON.parse(event.data);
    	setRefresh(data.update);
    }

    eventSource.onerror = (error)=> //em erro avisa no console e fecha a conexao
    {
		console.log("erro:", error)
		eventSource.close();
    }  

    }
    
    ,[])
  useEffect(()=>
	{
		if(Refresh=='True')
		{
			window.location.reload(); //recarrega a pagina
		}
	}
  ,[Refresh])  

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
