import streamlit as st
import pandas as pd
import plotly.express as px
from models import engine
df=pd.read_sql('select * from enderecos', engine)

st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown(""" 
            <style>
        /* Remove cabeçalho, rodapé e menu */
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
        """,
        unsafe_allow_html=True)

filtro=st.selectbox("Coluna:", options=["bairro","cidade"],index=1)
PessoasLocalizacao=df[filtro].value_counts().reset_index()


pizza = px.pie(PessoasLocalizacao,values='count', names=filtro,color_discrete_sequence=px.colors.sequential.Oranges)
pizza.update_layout(width=200,height=200, margin=dict(r=0,l=0,t=0,b=0))

st.plotly_chart(pizza)