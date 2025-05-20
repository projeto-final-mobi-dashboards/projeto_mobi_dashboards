import React from "react";
import PlotMap from "../mapa.jsx";
import PlotPie from "../endereco.jsx";
import PlotBar from "../curso.jsx";
import PlotGenderBar from "../genero.jsx";
import PlotIndicator from "../transport.jsx";
import Sideba from "../sidebar/index.jsx"
import "./Home.css";

export const Home = ()=>{
    return(
    <div className="MapDiv">
        <Sideba/>
        <PlotMap />

    </div>
    )
}
