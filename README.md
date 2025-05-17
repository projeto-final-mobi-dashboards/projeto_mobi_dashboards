> #### Sobre:

> Projeto contendo frontend feito com react, backend com flask e SQL_ALCHEMY para acessar o banco de dados mysql

> #### Objetivo:

> Análise de dados do aplicativo **MOBI**, criação de dashboards para visualização e retirada de insights
> Com opção de filtragem dos dados, exportação dos gráficos e figuras para diferentes meios tais como excel e pdf, atualização em tempo _quase_ real após alterações no banco de dados 
> Login e cadastro para controle de quem acessou a aplicação




## Contato:
#### Miguel: [github.com/MiguelDaSilvaGomes](https://github.com/MiguelDaSilvaGomes)
#### Gustavo: [github.com/GustavoProcopio27](https://github.com/GustavoProcopio27)




### Requer instalação de:
* ##### [Node.js](https://nodejs.org/en/download)
* ##### [Python](https://www.python.org/downloads/)
* ##### [MySQL](https://dev.mysql.com/downloads/installer/)

### Colaboradores, orientadores e desenvolvedores
| CARGO | PESSOA |
| ------ | ------ |
| PROFESSOR | Ulisses Roque Tomaz|
| PROFESSOR ORIENTADOR | Francisco Henrique de Freitas Viana|
| DESENVOLVEDOR | Miguel da Silva Gomes  |
| DESENVOLVEDOR | Gustavo Luiz da Silva Procópio |

### Dependências



#### Instalação de dependências a partir do requirements.txt ou pyproject.toml:

```bash
pip3 install -r requirements.txt
```

```bash
uv pip install
```

#### Baixar dependencias separadas:
```bash
pip3 install < nome da biblioteca >
```

```bash
uv pip install < nome da biblioteca >
```

#### Desinstalar dependencias:
```bash
pip3 uninstall < nome da biblioteca >
```

```bash
uv pip uninstall < nome da biblioteca >
```



#### Adicionar no requirements.txt ou no pyproject.toml:
```bash
pip3 freeze > requirements.txt
```


```bash
uv add < nome da biblioteca >


uv pip compile pyproject.toml > requirements.txt
```


```
projeto_mobi_dashboards
├─ backend
│  ├─ .python-version
│  ├─ app.py
│  ├─ blueprints
│  │  ├─ cadastro.py
│  │  ├─ cursosColunas.py
│  │  ├─ indicatorTransport.py
│  │  ├─ login.py
│  │  ├─ mapRoute.py
│  │  ├─ pieChartRoute.py
│  │  ├─ sent_event.py
│  │  ├─ usergenderBar.py
│  │  └─ verticalBar.py
│  ├─ dash
│  │  ├─ cursos.py
│  │  ├─ genero.py
│  │  ├─ indicator.py
│  │  ├─ map.py
│  │  ├─ models.py
│  │  ├─ pie.py
│  │  └─ __pycache__
│  │     └─ models.cpython-313.pyc
│  ├─ functions.py
│  ├─ models
│  │  └─ __init__.py
│  ├─ pyproject.toml
│  ├─ README.md
│  ├─ requirements.txt
│  └─ uv.lock
├─ frontend
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ public
│  │  ├─ favicon.ico
│  │  ├─ index.html
│  │  ├─ logo192.png
│  │  ├─ logo512.png
│  │  ├─ manifest.json
│  │  └─ robots.txt
│  ├─ README.md
│  └─ src
│     ├─ App.css
│     ├─ App.jsx
│     ├─ components
│     │  ├─ css
│     │  │  └─ loaderCSS.css
│     │  ├─ curso.jsx
│     │  ├─ endereco.jsx
│     │  ├─ genero.jsx
│     │  ├─ mapa.jsx
│     │  ├─ pageLoader.jsx
│     │  ├─ sidebar
│     │  │  ├─ index.jsx
│     │  │  └─ styles.css
│     │  └─ transport.jsx
│     ├─ Imagens
│     │  └─ logoapp.png
│     ├─ index.css
│     ├─ index.js
│     ├─ map.png
│     └─ reportWebVitals.js
├─ prediction_model
│  ├─ modelTraining.ipynb
|  ├─ predict_gender_randomforest_model.pkl
│  └─ names_dataset.csv
└─ README.md

```