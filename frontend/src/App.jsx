import React, { useEffect, useState } from 'react';

import Rotas from "./components/Routes/rotas.js";

import './App.css';

function App() {

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
        <Rotas />
    </div>
  );
}

export default App;
