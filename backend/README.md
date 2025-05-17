#### Informações importantes:

1. Gerenciador de pacotes utilizado está sendo uv

2. Conteudo do .env é a url de conexão com o banco de dados

### Ativação do ambiente virtual pelo comando :

```bash
.venv\Scripts\activate.bat
```

### Para usar o ambiente no VsCode:
1.Abra o Command Palette(Ctrl+Shift+P) e digite **_python:select interpreter_** 
2.Selecione o interpretar no ambiente, ou seja, no meu caso o caminho:

```bash
/backend/.venv/Scripts/python.exe
```


## Dependências e explicações do uso


#### Extensões do flask usadas:

1. Flask-CORS: Permite que um servidor web possa configurar quais são as origens (domínios) que podem acessar seus recursos

2. Flask-Session: habilita sessões via servidor, invés das sessões padrões do flask as quais armazenam os dados em _"signed cookies"_ , que são codificados e criptografados para previnir interferencia, assim ele não pode ser modificado sem o uso de uma chave secreta do servidor
 
3. Flask-Bcrypt: utilizado para fazer e checar hashs de senha, tendo maior integração com flask e abstração facilitando o uso de hash reduzindo (2 linha), to usando por integração mesmo, ela usa a bcrypt por baixo das coisas

4. Flask-Caching: Ainda nao botei nada com isso, mas adiciona suporte a operações e armazenamento em cache, aumenta a performance e escalabilidade, permitindo decidir o metodo de cacheamento(suportando até um servidor redis, overkill na minha opinião), e definir o tempo que uma rota fica na cache

#### Outras dependencias:
1.  Openpyxl : permite manipulação e criação de arquivos excel 
2.  Plotly: Criação de gráficos e figuras interativas com possibilidade de exportação para pdf, zoom e outras funções
3.  Streamlit: Utilizado para criação de filtros dinamicos para figuras e atualiza-las em tempo real
4.  Pandas: Manipulação e controle sobre os dados do banco e outras funções uteis, adoro esta biblioteca
5.  Joblib: Carrega o meu modelo de randomforest e processador de dados para leitura do modelo
6.  Requests: Possibilidade requisições facilitadas a apis externas e maior controle sobre o envio e retorno a elas
7.  SQLAlchemy e pymysql: Interface ORM(Object Relational Mapper) para acesso e interação com o banco de dados e conector ao banco de dados MySQL
8.  Unidecode: normalização de texto(nomes)
9.  Dotenv: Carrega conteudo do arquivo .env, util para guardar dados que serão frequentemente utilizados e nao podem ser vistos como a url de conexão ao banco de dados
10. Python-docx: biblioteca utilizada para gerar documentos word
11. FDDF/pypdf/reportlab:  Provavelmente a última dependência que será adiciona a não ser que haja outras necessidadades, utilizado para gerar pdfs, ainda tenho que escolher uma para utilizar

