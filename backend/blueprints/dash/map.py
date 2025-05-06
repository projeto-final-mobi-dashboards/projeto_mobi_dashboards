import pandas as pd
import streamlit as st
import plotly.express as px
from models import engine


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
df=pd.read_sql('select * from trecho', engine)
df["cidade"]=df["cidade"].str.lower().str.capitalize().str.strip()

map=px.scatter_map(df, lat='latitude', lon='longitude',color='cidade', hover_name='cidade',map_style="open-street-map", title="pontos nos trechos dos usuarios",color_discrete_sequence=px.colors.sequential.Hot ,zoom=8,center={'lat':-22.74628,'lon':-43.42604})
map.update_traces(marker={'size':15})  #seta o tamanho dos pontos no mapa

map.update_layout(margin= { "r":0,"t":0,"b":0,"l":0},legend_title="cidade",height=300)
st.plotly_chart(map)