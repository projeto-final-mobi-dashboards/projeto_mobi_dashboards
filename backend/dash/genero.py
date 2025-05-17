import pandas as pd
import plotly.express as px
import streamlit as st
from models import engine,process_gender_df

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

df_genero=process_gender_df(df)



barra=px.bar(df_genero, x='quantidade', y="genero",orientation='h', color="quantidade", color_continuous_scale=px.colors.sequential.OrRd)
barra.update_layout(height=300,width=500)


st.plotly_chart(barra)