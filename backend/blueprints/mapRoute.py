from flask import Blueprint,jsonify
import subprocess
import streamlit as st

mapBlueprint = Blueprint('mapa', __name__)

@mapBlueprint.route('/mapa', methods=['GET'])
def returnMap():

    subprocess.Popen(['streamlit', "run", "backend/blueprints/dash/map.py",'--server.port', '8505'])# essencialmente tudo na aplicação esta com subprocess.Popen para abrir o streamlit como subprocesso
    mapFrame='http://127.0.0.1:8505'
    return jsonify({'dash':mapFrame})