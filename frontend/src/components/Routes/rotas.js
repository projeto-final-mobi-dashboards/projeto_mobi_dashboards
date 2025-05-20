import { Routes, Route } from 'react-router-dom';
import Login from '../Login';
import { Home } from '../Home/Home';


export default function Rotas (){
    return(
        <Routes>
            <Route path="/" element={<Login />} />
            <Route path="/Home" element={<Home />}/>
        </Routes>

    );
}