from flask import Blueprint,jsonify
from subprocess import Popen

cursoBlueprint = Blueprint('curso', __name__)

@cursoBlueprint.route('/curso', methods=['GET'])
def returnBarChart():
    Popen(['streamlit', "run", "dash/cursos.py",'--server.port', '8502'])
    cursoFrame="http://127.0.0.1:8502"
    return jsonify({'dash':cursoFrame})