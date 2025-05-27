import React, { useState } from 'react';

export function Filter() {
  const tabelas = {
    usuarios: ['id', 'cargo', 'cpf', 'email_institucional', 'matricula', 'nome', 'termos'],
    enderecos: ['usuario_id', 'bairro', 'cep', 'cidade', 'numero', 'rua'],
    itinerarios: ['id', 'data', 'nome', 'usuario_id'],
    trechos: ['id', 'bairro', 'cidade', 'complemento', 'hora', 'latitude', 'local', 'longitude', 'meio_transporte', 'numero', 'rua', 'tipo_trajeto', 'itinerario_id']
  };

  const [selectedTables, setSelectedTables] = useState([]);
  const [selectedFields, setSelectedFields] = useState({});

  const handleTablesChange = (e) => {
    const options = Array.from(e.target.selectedOptions, option => option.value);
    setSelectedTables(options);

    // Limpa campos de tabelas não mais selecionadas
    setSelectedFields(prev => {
      const newFields = {};
      options.forEach(table => {
        if (prev[table]) {
          newFields[table] = prev[table];
        }
      });
      return newFields;
    });
  };

  const handleFieldsChange = (table, e) => {
    const options = Array.from(e.target.selectedOptions, option => option.value);
    setSelectedFields(prev => ({
      ...prev,
      [table]: options
    }));
  };

  const handleSubmit = () => {
    const payload = {
      tabelas: selectedTables,
      campos: selectedFields
    };

    console.log('Enviando:', payload);

    // Aqui você envia o payload para o backend (via fetch, axios, etc.)
  };

  return (
    <div className="filtros">
      <div>
        <label>Tabelas:</label>
        <select multiple value={selectedTables} onChange={handleTablesChange} className="comboTabelas">
          {Object.keys(tabelas).map((table) => (
            <option key={table} value={table}>
              {table}
            </option>
          ))}
        </select>
      </div>

      {selectedTables.map((table) => (
        <div key={table}>
          <label>Campos para {table}:</label>
          <select
            multiple
            value={selectedFields[table] || []}
            onChange={(e) => handleFieldsChange(table, e)}
          >
            {tabelas[table].map((field) => (
              <option key={field} value={field}>
                {field}
              </option>
            ))}
          </select>
        </div>
      ))}

      <button
        onClick={handleSubmit}
        disabled={!selectedTables.length || Object.values(selectedFields).every(fields => fields.length === 0)}
      >
        Enviar
      </button>
    </div>
  );
}


