#bibliotecas
from flask import Flask
from models import bcrypt,cors,session, database_url, engine
from functions import register_Blueprints
#database url
from secrets import token_bytes#,token_urlsafe

#blueprints



def create_app():
    app=Flask(__name__)

    #configurações da aplicação
    app.config['SQLALCHEMY_DATABASE_URI']=database_url
    app.config['SESSION_TYPE'] = 'sqlalchemy'
    app.config['SESSION_SQLALCHEMY'] = engine

    
    app.config['SECRET_KEY']=token_bytes(16)


    #inicia as extensões
    bcrypt.init_app(app)
    cors.init_app(app)
    session.init_app(app)
    
    #registras as blueprints
    register_Blueprints(app)

    return app


if __name__ == "__main__":
    app=create_app()
    app.run(debug=True)
