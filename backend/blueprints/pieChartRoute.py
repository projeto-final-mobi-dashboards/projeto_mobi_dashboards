from flask import Blueprint,jsonify
import subprocess

adressesBlueprint = Blueprint('endereco', __name__)

@adressesBlueprint.route('/enderecos', methods=['GET'])
def returnPie():
    subprocess.Popen(['streamlit', "run", "backend/blueprints/dash/pie.py",'--server.port','8503'])# essencialmente tudo na aplicação esta com subprocess.Popen para abrir o streamlit como subprocesso
    pieFrame="http://127.0.0.1:8503"
    return jsonify({'dash':pieFrame})