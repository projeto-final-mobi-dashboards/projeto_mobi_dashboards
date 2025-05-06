import React, {useState, useEffect} from 'react';
import Loader from './pageLoader.jsx';

export default function PlotBar()
{
    const [url,setURL] = useState(null);
    useEffect(
          ()=>{
              fetch('/curso')
              .then(res=> res.json())
              .then(data => {console.log(data);setURL(data.dash);});
            },[]);
    if(!url)
    {      
        return (<Loader/>);
    }
    return(   
            <div>
              <iframe src={url} title="Gráfico de usuários por curso" width='1200' height='300'></iframe>
            </div>
          ) 

}