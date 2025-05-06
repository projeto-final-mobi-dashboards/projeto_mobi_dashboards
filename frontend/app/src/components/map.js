import React, {useState, useEffect} from 'react';
import Plot from 'react-plotly.js'
import './map.css'

export default function PlotMap()
{
    const [plot,setPlot] = useState(null);
    useEffect(
          ()=>{
              fetch('/trecho')
              .then(res=> res.json())
              .then(data => {setPlot(data);});
            },[]);
    if(!plot)
    {      
        return (
        
        <div class="text">Loading...</div>
        
      );
    }
    return(   
            <div className='Mapa'>
              
              <Plot data={plot.data} layout={plot.layout}/>
            </div>
          ) 

}