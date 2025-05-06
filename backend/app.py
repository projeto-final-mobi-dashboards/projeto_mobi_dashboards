from flask import Flask,request,session,url_for,redirect
from models import db
from dotenv import load_dotenv
import os
from secrets import token_bytes#,token_urlsafe
from blueprints.trecho import trecho_blueprint
from blueprints.enderecos import endereco_blueprint
from blueprints.cursos import curso_blueprint
from blueprints.genero import gender_blueprint
load_dotenv(dotenv_path='/home/mestridmid/Documentos/Dashboard/projeto_mobi_dashboards-main/backend/.env')


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']=token_bytes(16)

    app.register_blueprint(trecho_blueprint)
    app.register_blueprint(endereco_blueprint)
    app.register_blueprint(curso_blueprint)
    app.register_blueprint(gender_blueprint)
    

    db.init_app(app)

    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)
