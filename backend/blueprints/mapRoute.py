from flask import Blueprint,jsonify
import subprocess

mapBlueprint = Blueprint('mapa', __name__)

@mapBlueprint.route('/mapa', methods=['GET'])
def returnMap():

    subprocess.Popen(['streamlit', "run", "dash/map.py",'--server.port', '8505'])
    mapFrame='http://127.0.0.1:8505'
    return jsonify({'dash':mapFrame})