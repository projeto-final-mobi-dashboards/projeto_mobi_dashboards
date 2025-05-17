from flask import Blueprint,jsonify
import subprocess

genderBlueprint = Blueprint('gender', __name__)

@genderBlueprint.route('/genero', methods=['GET'])
def returnHorizontalBar():
    subprocess.run(['streamlit', "run", "dash/genero.py",'--server.port','8504'])
    horizontal_barFrame="http://127.0.0.1:8504"
    return jsonify({'dash':horizontal_barFrame})