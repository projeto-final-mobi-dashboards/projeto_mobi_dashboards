from sqlalchemy import create_engine
from dotenv import load_dotenv
from os import getenv

load_dotenv(dotenv_path='backend/.env')

database_url=getenv('DATABASE_URL')
engine=create_engine(database_url)






from pandas import DataFrame
from joblib import load
from unidecode import unidecode
from os.path import abspath,join,dirname
def process_gender_df(data: DataFrame):
    base_dir=abspath(join(dirname(__file__), "..",".."))
    gender_model_path=join(base_dir,"prediction_model","predict_gender_randomforest_model.pkl")

    df=data
    processadorColuna,modelo_floresta=load(gender_model_path)

    df['primeiro nome']=data['nome'].str.split(' ').str[0].str.capitalize().apply(unidecode)

    #separa as letras
    df["first_letter"] = df['primeiro nome'].str[:1]  
    df["first_two_letters"] = data['primeiro nome'].str[:2]  
    df["last_letter"] = data['primeiro nome'].str[-1:]
    df["last_two_letters"] = data['primeiro nome'].str[-2:] 

    #separada os dados utilizados para previsão
    Pred_data=df[['primeiro nome','first_letter','first_two_letters','last_letter','last_two_letters']]

    dados=processadorColuna.transform(Pred_data) # converte eles



    previsaoNova=modelo_floresta.predict(dados) # faz previsão
    df['genero']=previsaoNova #bota no dataframe


    dicionario={
    0:'feminino',
    1:'masculino'
    }

    df['genero']=df['genero'].map(dicionario) # substitui para algo legivel

    df.drop(columns=['first_letter','first_two_letters','last_letter','last_two_letters','senha','email_institucional','cpf'], inplace=True)
    df_genero=df.groupby(by=['genero'])['cargo'].value_counts().reset_index()
    df_genero.columns=['genero','cargo','quantidade']

    return df_genero