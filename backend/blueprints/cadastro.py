from flask import Blueprint,request, jsonify
from models import Administrador, engine
from sqlalchemy.orm import Session
from flask_bcrypt import generate_password_hash

loginBlueprint = Blueprint("logar", __name__)
def hash(password:str):
    return generate_password_hash(password).decode('utf-8')

@loginBlueprint.route("/cadastro", method=["GET", "POST"])
def cadastro():
    try:
        data=request.get_json()

        nome=data.get('name')
        telefone=data.get('name')
        matricula=data.get("name")
        email_instituicional=data.get("name")
        senha=hash(data.get("name"))
        termo=data.get('name')


        
    except:
        resp="False"
        raise Exception("Erro na aquisição dos dados")
    
    else: # se nao pega exceção vai para ca
        with Session(engine) as session:
            try:
                adm = Administrador( #instancia a classe administrador
                    nome = nome,
                    email_instituicional=email_instituicional,
                    matricula=matricula,
                    telefone=telefone,
                    termo=termo,
                    senha=senha,
                    Masterstatus=False
                    )
                session.add(adm) #meio que binda o objeto
            except:
                session.rollback()
                resp="false"
                print("erro na inserção")
            else:
                session.commit() #commita a mudança ao banco
                resp="True"



    return jsonify({"resposta":resp}) # responde com true se foi

