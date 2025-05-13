from flask import Blueprint,jsonify
import subprocess 

transportBlueprint = Blueprint('indicator', __name__)

@transportBlueprint.route('/transporte', methods=['GET'])
def returnIndicator():
    subprocess.Popen(['streamlit', "run", "backend/blueprints/dash/indicator.py",'--server.port', '8501']) # essencialmente tudo na aplicação esta com subprocess.Popen para abrir o streamlit como subprocesso
    transportFrame='http://127.0.0.1:8501'
    return jsonify({'dash':transportFrame})