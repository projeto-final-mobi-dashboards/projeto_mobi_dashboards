# Um arquivo __init__.py contem codigo que será executado quando ocorrer importações do modulo do pacote
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import BIT

db=SQLAlchemy()

class Enderecos(db.Model):
    __tablename__='enderecos'

    usuario_id =db.Column(db.Integer, db.ForeignKey('usuarios.id'), primary_key = True)
    bairro = db.Column(db.String(50), nullable=False)
    cep = db.Column(db.String(50), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    numero = db.Column(db.String(100), nullable=False)
    rua = db.Column(db.String(100), nullable=False)

    #usuario = db.relationship('enderecos', backref=db.backref('usuarios'), lazy='joined')

    def __repr__(self):
        return f'cep: {self.cep} , cidade: {self.cidade}, bairro: {self.bairro}, rua: {self.rua}'




class Usuarios(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key = True)
    cargo = db.Column(db.String(50), nullable = False ) 
    cpf = db.Column(db.String(50), nullable = False ) 
    email_instituicional = db.Column(db.String(100), nullable = False) 
    matricula = db.Column(db.String(20), nullable = False) 
    nome = db.Column(db.String(100), nullable = False ) 
    senha = db.Column(db.String(256), nullable = False ) 
    termos = db.Column(BIT(1), nullable = False ) 

    def __repr__(self):
        return f'Cargo: {self.cargo}, CPF : {self.cpf}, Email : {self.email_instituicional} '
   

class Itinerario(db.Model):
    __tablename__='itinerarios' 

    id = db.Column(db.Integer, primary_key = True) 
    data = db.Column(db.String(255), nullable = False ) 
    nome = db.Column(db.String(255), nullable = False )
    usuario_id = db.Column(db.Integer,db.ForeignKey('usuarios.id'), nullable = False)  

    #usuario = db.relationship('usuarios', backref=db.backref('itinerarios'), lazy='joined')

    def __repr__(self):
        return f'data: {self.data}, nome : {self.nome},'



class Trecho(db.Model):
    __tablename__='trecho'

    id = db.Column(db.Integer, primary_key = True)
    bairro = db.Column(db.String(200) , nullable=False )
    cidade = db.Column(db.String(200), nullable = False ) 
    complemento = db.Column(db.String(200),nullable=True)
    hora = db.Column(db.String(200), nullable = False ) 
    latitude = db.Column(db.Double, nullable = False ) 
    local = db.Column(db.String(200), nullable = False ) 
    longitude = db.Column(db.Double, nullable = False ) 
    meio_transporte = db.Column(db.String(200), nullable = False ) 
    numero = db.Column(db.String(200), nullable = False ) 
    rua = db.Column(db.String(200), nullable = False ) 
    tipo_trajeto = db.Column(db.String(255), nullable = False ) 
    itinerario_id = db.Column(db.Integer,db.ForeignKey('Itinerario.id')) 

    #itinerario = db.relationship('itinerarios', backref=db.backref('trecho'), lazy='joined')

    def __repr__(self):
        return f' latitude : {self.latitude}, longitude: {self.longitude}, cidade: {self.cidade}'


