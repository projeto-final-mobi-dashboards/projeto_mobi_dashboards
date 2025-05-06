import { Sidebar, Menu, MenuItem } from 'react-pro-sidebar';
import logo from "../../Imagens/logoapp.png";
import { FaHome, FaChartBar, FaTable, FaFileAlt, FaInfoCircle, FaSun, FaMoon } from 'react-icons/fa';
import { useState, useEffect, useRef } from 'react';
import "./styles.css";

export default function Sideba() {
  const [isDarkMode, setIsDarkMode] = useState(false);
  const sidebarRef = useRef(null);

  const toggleTheme = () => {
    setIsDarkMode(!isDarkMode);
    // Aqui você pode adicionar lógica para alterar o tema da aplicação
  };
  useEffect(() => {
    const sidebarDiv = sidebarRef.current?.querySelector('.css-dip3t8');
    if (sidebarDiv) {
    sidebarDiv.style.setProperty('transition', 'background-color 0.3s ease', 'important');
    sidebarDiv.style.setProperty(
        'background-color',
        isDarkMode ? '#1a2238' : '#ffffff',
        'important'
      );
    }
  }, [isDarkMode]);

  return (
    <>
    <div ref={sidebarRef}>
      <Sidebar
        style={{
            height: '100vh',
            color: isDarkMode ? '#fff' : '#000',
        }}
      >
        <div style={{ padding: '20px', textAlign: 'left', display: 'flex' }}>
          <img src={logo} alt="Logo Mobi" style={{ width: '60px', marginBottom: '10px' }} />
          <div style={{ flexDirection: 'column', marginLeft: '10px' }}>
            <h2 style={{ margin: 5, fontSize: '18px' }}>Mobi</h2>
            <p style={{ margin: 5, fontSize: '18px', color: '#ccc' }}>Dashboard</p>
          </div>
        </div>
        <Menu iconShape="circle">
          <MenuItem icon={<FaHome />}> Home </MenuItem>
          <MenuItem icon={<FaChartBar />}> Gráficos </MenuItem>
          <MenuItem icon={<FaTable />}> Tabelas </MenuItem>
          <MenuItem icon={<FaFileAlt />}> Relatórios </MenuItem>
          <MenuItem icon={<FaInfoCircle />}> Sobre </MenuItem>
        </Menu>
        <div style={{ marginTop: 'auto', padding: '20px' }}>
          <button
            onClick={toggleTheme}
            style={{
              width: '100%',
              padding: '10px',
              backgroundColor: isDarkMode ? '#364fc7' : '#eee', // tom mais claro de azul
              color: isDarkMode ? '#fff' : '#000',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
              marginTop: "90vh"
            }}
          >
            {isDarkMode ? <FaSun /> : <FaMoon />} {isDarkMode ? 'Modo Claro' : 'Modo Escuro'}
          </button>
        </div>
      </Sidebar>
      </div>
    </>
  );
}
