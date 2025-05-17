import React, {useState, useEffect} from 'react';
import Loader from './pageLoader.jsx';


export default function PlotGenderBar()
{
    const [url,setURL] = useState(null);
    useEffect(
          ()=>{
              fetch('/genero')
              .then(res=> res.json())
              .then(data => {setURL(data.dash);});
            },[]);
    if(!url)
    {      
        return (<Loader/>);
    }
    return(   
            <div>
              <iframe src={url} title="Gráfico de usuários por gênero" width='500' height='300' ></iframe>
            </div>
          ) 

}