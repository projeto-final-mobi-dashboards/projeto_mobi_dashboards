import React, { useEffect, useState } from 'react';

import PlotMap from "./components/mapa.jsx";
import PlotPie from "./components/endereco.jsx";
import PlotBar from "./components/curso.jsx";
import PlotGenderBar from "./components/genero.jsx";
import PlotIndicator from "./components/transport.jsx"
import Login from "./components/Login"

import Sideba from "./components/sidebar/index.jsx"
import './App.css';

function App() {
  useEffect(
    ()=>{ //Algo aqui ta errado, nao sei oq
    const eventSource= new EventSource("/refreshEvent")

    eventSource.onmessage = (event)=>{
      try{
    	const data = JSON.parse(event.data);
      console.log("Recebido:", data)

      if(data.update==true)
		  {
        console.log("Foi")
        window.location.reload(); //recarrega a pagina
		  }


      }
      catch(error){console.log("Erro em algo:", error)}
    }

    eventSource.onerror = (error)=>{
      console.log("erro:", error)
    }  

    }
    
    ,[])
  // useEffect(()=>
	// {
	// 	if(Refresh=='True')
	// 	{
  //     console.log("Foi")
	// 		window.location.reload(); //recarrega a pagina
	// 	}
	// }
  // ,[Refresh])  

  return (
    <div >
        <Login/>
    </div>
  );
}

export default App;
