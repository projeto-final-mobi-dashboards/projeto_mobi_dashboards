import React from 'react';
import './css/loaderCSS.css';


export default function Loader()
{
return(   
    <div className="loader">
    <svg width="120" height="120" viewBox="0 0 100 100">
        {/* Marker */}
      <defs>
        <mask id="hole-mask">
          <rect width="100%" height="100%" fill="white" />
          <circle cx="50" cy="40" r="20" fill="black" />
        </mask>
      </defs>

      <path d="M50 0C30 0 15 20 15 40c0 20 35 60 35 60s35-40 35-60C85 20 70 0 50 0z" 
            fill="white" mask="url(#hole-mask)" />

      <g className="rotating-arrow">{/*seta girando */}
        <polygon points="50,20 42,40 50,36 58,40" fill="black"/>
      </g>
    </svg>
    </div>       
) 

}