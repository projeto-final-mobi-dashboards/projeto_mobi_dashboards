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
from blueprints.sent_event import sent_eventBlueprint
load_dotenv(dotenv_path='backend/.env')

    
def create_app():
    app=Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY']=token_bytes(16)

    app.register_blueprint(cursoBlueprint) #registras blueprints onde serão acessadas as outras rotas
    app.register_blueprint(adressesBlueprint)
    app.register_blueprint(mapBlueprint)
    app.register_blueprint(genderBlueprint)
    app.register_blueprint(transportBlueprint)
    app.register_blueprint(sent_eventBlueprint)
    db.init_app(app) 

    return app




if __name__ == "__main__":
    app=create_app()
    app.run(debug=True, threaded=True) # talvez seja necessario retirar true do debug, ver para,etrps disso, aparentemente ele tem load dotenv? wtf
