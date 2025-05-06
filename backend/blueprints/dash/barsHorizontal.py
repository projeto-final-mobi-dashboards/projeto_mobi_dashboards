import pandas as pd
import plotly.express as px
import streamlit as st
from models import engine
from unidecode import unidecode
from joblib import load

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown(""" 
        <style>

         header, footer, .stDeployButton, #MainMenu {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Remove o padding padrão da página */
        .block-container {
            padding: 0rem !important;
        }
        .main {
            background: #1a2238;
        }
        </style>  
        """ , unsafe_allow_html=True
)
df=pd.read_sql_query('select * from usuarios', engine)

processadorColuna,modelo_floresta=load('prediction_model/predict_gender_randomforest_model.pkl')

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
df_genero=namesdf.groupby(by=['genero'])['cargo'].value_counts().reset_index()
df_genero.columns=['genero','cargo','quantidade']

barra=px.bar(df_genero, x='quantidade', y="genero", color="quantidade", orientation='h',color_continuous_scale=px.colors.sequential.OrRd)
barra.update_layout(height=300,width=500)
st.plotly_chart(barra)