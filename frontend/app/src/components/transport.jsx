import React, {useState, useEffect} from 'react';
import Loader from './pageLoader.jsx'


export default function PlotIndicator()
{
    const [url,setURL] = useState(null);
    useEffect(
          ()=>{
              fetch('/transporte')
              .then(res=> res.json())
              .then(data => {console.log(data);setURL(data.dash);});
            },[]);
    if(!url)
    {      
        return ( <Loader/> );
    }
    return(   
            <div className='divTransportIndicator'>
                <iframe src={url} width="700" height="300"  title='Transportes' style={{border:'none'}}></iframe>
            </div>
          ) 

}