from flask import Blueprint
import pandas as pd
from plotly.express import bar
from plotly.io import to_json
from models import db
from dotenv import load_dotenv
from os import getenv
import requests
from unidecode import unidecode

import joblib


load_dotenv("/home/mestridmid/Documentos/Dashboard/projeto_mobi_dashboards-main/backend/.env")
gender_blueprint = Blueprint('genero', __name__)

@gender_blueprint.route('/genero', methods=['GET'])
def read():
    engine = db.get_engine()

    df=pd.read_sql_query('select * from usuarios', engine)

    processadorColuna,modelo_floresta=joblib.load('/home/mestridmid/Documentos/Dashboard/projeto_mobi_dashboards-main/prediction_model/predict_gender_randomforest_model.pkl')

    df.drop(columns=['cpf','email_institucional','matricula','senha','termos'])
    namesdf=df
    namesdf['primeiro nome']=df['nome'].str.split(' ').str[0].str.capitalize().apply(unidecode)

    
    namesdf["first_letter"] = namesdf['primeiro nome'].str[:1]  
    namesdf["first_two_letters"] = namesdf['primeiro nome'].str[:2]  

    namesdf["last_letter"] = namesdf['primeiro nome'].str[-1:]    
    namesdf["last_two_letters"] = namesdf['primeiro nome'].str[-2:] 

    Pred_data=namesdf[['primeiro nome','first_letter','first_two_letters','last_letter','last_two_letters']]



    dados=processadorColuna.transform(Pred_data)



    previsaoNova=modelo_floresta.predict(dados)
    namesdf['genero']=previsaoNova


    dicionario={
        0:'feminino',
        1:'masculino'
        }

    namesdf['genero']=namesdf['genero'].map(dicionario)

    namesdf.drop(columns=['first_letter','first_two_letters','last_letter','last_two_letters','senha','email_institucional','cpf'], inplace=True)
    print(namesdf)
    df_genero=namesdf.groupby(by=['genero'])['cargo'].value_counts().reset_index()
    df_genero.columns=['genero','cargo','quantidade_aproximada']
    print(df_genero)

    fig=bar(df_genero, x='quantidade_aproximada', y="genero", color="quantidade_aproximada", orientation='h')
    figJson=to_json(fig, pretty=True)

    return figJson

