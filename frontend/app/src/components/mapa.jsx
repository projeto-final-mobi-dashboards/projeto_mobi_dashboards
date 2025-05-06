import React, {useState, useEffect} from 'react';
import Loader from './pageLoader.jsx';

export default function PlotMap()
{
    const [url,setURL] = useState(null);
    useEffect(
          ()=>{
              fetch('/mapa')
              .then(res=> res.json())
              .then(data => { console.log(data);setURL(data.dash);});
            },[]);
    if(!url)
    {      
        return (<Loader/>);
    }
    return(   
            <div className='divMapa'>   
              <iframe src={url} width='800' height='320'></iframe>
            </div>
          ) 

}