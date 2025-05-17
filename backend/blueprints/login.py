from flask import Blueprint,session, request, jsonify
from models import Administrador
from flask_bcrypt import check_password_hash

loginBlueprint = Blueprint("logar", __name__)

def set_Session(db_data):
    session['matricula']=db_data.matricula
    session['cpf']=db_data.cpf
    session['email']=db_data.email_institucional
    session['telefone']=db_data.telefone

    return None
    

@loginBlueprint.route('/logar', methods=["GET","POST"])
def logar():
    data=request.get_json()
    matricula=data.get("name")
    email=data.get("name")
    senha=data.get("name")
    resp="False"

    db_data=Administrador.query().filter( Administrador.email_institucional==email,Administrador.matricula==matricula) # conferir o retorno daqui
    if db_data:
        try:
            senhaHash=db_data.senha # aqui seria o retorno do banco, tenho que ver direito o query em casa, eu devia ter estudado isso kkkkkkkkkk
            if check_password_hash(senhaHash,senha):
                set_Session(db_data)
                resp="True"                
        except Exception as ex:
            print(f"Erro ocorrido: {ex}")
    else:
        print("erro na consulta")
    
    return jsonify({'resposta':resp})
