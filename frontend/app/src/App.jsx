import React, { useState,useEffect } from 'react';

import PlotMap from "./components/mapa.jsx";
import PlotPie from "./components/endereco.jsx";
import PlotBar from "./components/curso.jsx";
import PlotGenderBar from "./components/genero.jsx";
import PlotIndicator from "./components/transport.jsx"

import Sideba from "./components/sidebar/index.jsx"
import './App.css';

function App() {
  const [Refresh,setRefresh]=useState('')
  useEffect( () =>
  {
    const refresh_event = new EventSource("/refreshEvent") // de onde recebe o evento
    refresh_event.onmessage = (event) => //tipo de evento que ocorre quando uma mensagem é recebida pelo event souce
    { 
    	const data = JSON.parse(event.data) 
		const ExistsNewData = data.update
    	setRefresh(ExistsNewData) //seta o valor na variavel
    }
    

	refresh_event.onerror = ()=> 
	{
		refresh_event.close() //em caso de erro feche o canal de comunicação
	}
  }, [])

  useEffect( () =>{
	if(Refresh == 'True') //se for verdadeiro, recarrega a pagina
	{
		window.location.reload(false)
	}


  },[Refresh])

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
