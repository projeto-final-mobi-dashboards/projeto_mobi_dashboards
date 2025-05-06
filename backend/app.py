#bibliotecas
from flask import Flask
from models import db
from dotenv import load_dotenv

#database url
from os import getenv
from secrets import token_bytes#,token_urlsafe

#blueprints
from blueprints.usergenderBar import genderBlueprint
from blueprints.indicatorTransport import transportBlueprint
from blueprints.mapRoute import mapBlueprint
from blueprints.pieChartRoute import adressesBlueprint
from blueprints.verticalBar import cursoBlueprint
load_dotenv(dotenv_path='backend/.env')


def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']=token_bytes(16)

    app.register_blueprint(cursoBlueprint)
    app.register_blueprint(adressesBlueprint)
    app.register_blueprint(mapBlueprint)
    app.register_blueprint(genderBlueprint)
    app.register_blueprint(transportBlueprint)

    db.init_app(app)

    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)
