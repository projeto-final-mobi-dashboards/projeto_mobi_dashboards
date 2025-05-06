import React, {useState, useEffect} from 'react';
import Plot from 'react-plotly.js'


export default function Gender()
{
    const [plot,setPlot] = useState(null);
    useEffect(
          ()=>{
              fetch('/genero')
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
            <div>
              <Plot data={plot.data} layout={plot.layout}/>
            </div>
          ) 

}