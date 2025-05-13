import plotly.express as px
import pandas as pd
import streamlit as st
from models import engine


st.set_page_config(layout="wide", initial_sidebar_state="collapsed")
st.markdown(""" 
            <style>

        /* Reduz padding interno das colunas */
        .css-1kyxreq {
            gap: 0rem !important;
            margin: 0rem !important;
        }
        
        /* Colunas sem padding ou margem */
        div[data-testid="column"] {
            padding: 0rem !important;
            margin: 0rem !important;
        }
            
        /* Remove cabeçalho, rodapé e menu */
        header, footer, .stDeployButton, #MainMenu {
            display: none !important;
            visibility: hidden !important;
        }
        
        /* Remove o padding padrão da página */
        .block-container {
            padding: 0rem !important;
        }
                .stMultiSelect {
            max-width: 200px !important;
            width: 200px !important;
        }
            


            

        div[data-baseweb="select"] {
            max-width: 200px !important;
            width: 200px !important;
        }

        /* Reduz altura e espaçamento dos itens selecionados */
        .stMultiSelect [data-baseweb="tag"] {
            margin: 0 2px 2px 0;
            height: 24px;
        }

        /* Ajuste na altura da área de entrada */
        .stMultiSelect input {
            height: 10px;
            font-size: 24px;
        }
            
        .main{
            background: #1a2238;
        }
        """, unsafe_allow_html=True)

col1, col2 = st.columns([1,1])

df=pd.read_sql('select * from usuarios', engine)


df['curso']=df["matricula"].str.replace(r'\d+', '', regex=True)

dicio={
"EPROD": "Engenharia de produção",
"EMEC": "Engenharia mecanica",
"ECAN": "Engenharia controle",
"INFINI": "Informática",
"TELINI": "Telecomunicação",
"AUTNI": "Automação industrial",
"ENFINI": "Enfermagem"
}
df['curso']=df['curso'].map(dicio)
df.drop(columns=['matricula', 'senha','email_institucional'], inplace=True)

df_curso=df.groupby(by=['curso'])['cargo'].value_counts().reset_index()
df_curso.columns=["curso","cargo","quantidade"]

#print(df_curso)
with col1:
    filter=st.multiselect("selecione um curso para filtrar",options=list(df_curso['curso']), default=['Informática','Enfermagem','Automação industrial','Telecomunicação'])

df_curso=df_curso.loc[df_curso['curso'].isin(filter)]


with col2:
    bars=px.bar(df_curso,x='curso', y='quantidade', orientation='h' ,color='quantidade',color_continuous_scale=px.colors.sequential.OrRd)
    bars.update_layout(xaxis_title="cursos do cefet" , yaxis_title="quantidade de alunos",width=10,height=200, margin=dict(r=0,l=0,b=0,t=0))
    st.plotly_chart(bars, use_container_width=True)