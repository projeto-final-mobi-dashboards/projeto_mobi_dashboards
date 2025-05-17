# Um arquivo __init__.py contem codigo que será executado quando ocorrer importações do modulo do pacote

#sql alchemy
from sqlalchemy import create_engine,Column,Integer,String,Double,ForeignKey
from sqlalchemy.orm import declarative_base 
from sqlalchemy.dialects.mysql import BIT

# outras coisas
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from flask_session import Session as flaskSession
# pegar a url da database
from dotenv import load_dotenv
from os import getenv





load_dotenv(dotenv_path='backend/.env')

database_url=getenv('DATABASE_URL')
engine=create_engine(database_url)

conexao=engine.connect()
Base=declarative_base()


session=flaskSession()
bcrypt = Bcrypt()
cors=CORS()


class Enderecos(Base):
    __tablename__='enderecos'

    usuario_id =Column(Integer, ForeignKey('usuarios.id'), primary_key = True)
    bairro = Column(String(50), nullable=False)
    cep = Column(String(50), nullable=False)
    cidade = Column(String(100), nullable=False)
    numero = Column(String(100), nullable=False)
    rua = Column(String(100), nullable=False)

    #usuario = relationship('enderecos', backref=backref('usuarios'), lazy='joined')

    def __repr__(self):
        return f'cep: {self.cep} , cidade: {self.cidade}, bairro: {self.bairro}, rua: {self.rua}'




class Usuarios(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key = True)
    cargo = Column(String(50), nullable = False ) 
    cpf = Column(String(50), nullable = False ) 
    email_institucional = Column(String(100), nullable = False) 
    matricula = Column(String(20), nullable = False) 
    nome = Column(String(100), nullable = False ) 
    senha = Column(String(256), nullable = False ) 
    termos = Column(BIT(1), nullable = False ) 

    def __repr__(self):
        return f'Cargo: {self.cargo}, CPF : {self.cpf}, Email : {self.email_instituicional} '
   

class Itinerario(Base):
    __tablename__='itinerario' 

    id = Column(Integer, primary_key = True) 
    data = Column(String(255), nullable = False ) 
    nome = Column(String(255), nullable = False )
    usuario_id = Column(Integer,ForeignKey('usuarios.id'), nullable = False)  

    #usuario = relationship('usuarios', backref=backref('itinerarios'), lazy='joined')

    def __repr__(self):
        return f'data: {self.data}, nome : {self.nome},'



class Trecho(Base):
    __tablename__='trecho'

    id = Column(Integer, primary_key = True)
    bairro = Column(String(200) , nullable=False )
    cidade = Column(String(200), nullable = False ) 
    complemento = Column(String(200),nullable=True)
    hora = Column(String(200), nullable = False ) 
    latitude = Column(Double, nullable = False ) 
    local = Column(String(200), nullable = False ) 
    longitude = Column(Double, nullable = False ) 
    meio_transporte = Column(String(200), nullable = False ) 
    numero = Column(String(200), nullable = False ) 
    rua = Column(String(200), nullable = False ) 
    tipo_trajeto = Column(String(255), nullable = False ) 
    itinerario_id = Column(Integer,ForeignKey('Itinerario.id')) 

    #itinerario = relationship('itinerarios', backref=backref('trecho'), lazy='joined')

    def __repr__(self):
        return f' latitude : {self.latitude}, longitude: {self.longitude}, cidade: {self.cidade}'

class Administrador(Base):
    __tablename__='administradores'

    id = Column(Integer, nullable=False,primary_key= True)
    nome = Column(String(100), nullable=False)
    email_institucional = Column(String(100), nullable=False)
    senha = Column(String(255), nullable=False)
    matricula = Column(String(20), nullable=False)
    telefone = Column(String(30), nullable=False)
    termos = Column(BIT(1), nullable = False ) 
    Masterstatus = Column(BIT(1), nullable = False ) 

    def __repr__(self):
        return f' nome : {self.email}, matricula: {self.matricula}, telefone: {self.telefone}'
    

