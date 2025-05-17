from flask import Blueprint,jsonify
import subprocess

transportBlueprint = Blueprint('indicator', __name__)

@transportBlueprint.route('/transporte', methods=['GET'])
def returnIndicator():
    subprocess.Popen(['streamlit', "run", "dash/indicator.py",'--server.port', '8501'])
    transportFrame='http://127.0.0.1:8501'
    return jsonify({'dash':transportFrame})
