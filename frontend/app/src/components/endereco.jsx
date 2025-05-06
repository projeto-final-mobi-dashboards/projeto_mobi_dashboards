import React, {useState, useEffect} from 'react';
import Loader from './pageLoader.jsx';


export default function PlotPie()
{
    const [url,setURL] = useState(null);
    useEffect(
          ()=>{
              fetch('/enderecos')
              .then(res=> res.json())
              .then(data => {console.log(data);setURL(data.dash);});
            },[]);
    if(!url)
    {      
        return (<Loader/>);
    }
    return(   
            <div>
              <iframe src={url} title="gráfico de usuários por bairro/cidade" width='400' height='320'></iframe>
            </div>
          ) 

}