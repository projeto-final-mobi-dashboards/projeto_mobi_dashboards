from flask import Blueprint,jsonify
import subprocess

genderBlueprint = Blueprint('gender', __name__)

@genderBlueprint.route('/genero', methods=['GET'])
def returnHorizontalBar():
    subprocess.run(['streamlit', "run", "backend/blueprints/dash/barsHorizontal.py",'--server.port','8504'])# essencialmente tudo na aplicação esta com subprocess.Popen para abrir o streamlit como subprocesso
    horizontal_barFrame="http://127.0.0.1:8504"
    return jsonify({'dash':horizontal_barFrame})