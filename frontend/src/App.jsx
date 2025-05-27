import React from 'react';

import Rotas from "./components/Routes/rotas.js";



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
