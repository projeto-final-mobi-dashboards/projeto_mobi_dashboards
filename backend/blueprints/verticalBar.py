from flask import Blueprint,jsonify
import subprocess

cursoBlueprint = Blueprint('curso', __name__)

@cursoBlueprint.route('/curso', methods=['GET'])
def returnBarChart():
    subprocess.Popen(['streamlit', "run", "backend/blueprints/dash/barsVertical.py",'--server.port', '8502'])
    cursoFrame="http://127.0.0.1:8502"
    return jsonify({'dash':cursoFrame})