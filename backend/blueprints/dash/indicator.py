import pandas as pd
import streamlit as st
from plotly.graph_objects import  Figure, Indicator
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
        
            
            
        /* Estilo para o multiselect e selectbox */
        .stSelectbox {
            width: 200px !important;
            font-size: 12px !important;
            padding: 0.25rem !important;
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
        .main
            {background: #1a2238;
        }
    </style>
""",unsafe_allow_html=True
)

query='select tr.meio_transporte,tr.tipo_trajeto from trecho as tr,itinerario as it,usuarios as us where tr.itinerario_id=it.id and it.usuario_id=us.id;'
dfTotal=pd.read_sql(query, engine)
dfTotal=dfTotal.groupby(by=['meio_transporte']).value_counts().reset_index()
dfTotal["porcentagem"]=100*(dfTotal['count']/(dfTotal['count'].sum()))
dfTotal["porcentagem"]=dfTotal["porcentagem"].round(2)

dfTotal.columns=["transporte","trajeto","quantidade","porcentagem"]

listaTrajetos=dfTotal['trajeto'].unique()
listaTransportes=dfTotal['transporte'].unique()

col1, col2 = st.columns([1,1])
with col1:
    filter1= st.multiselect('Selecione o trajeto:', options=listaTrajetos,default="Ida")
    filter2= st.selectbox('Selecione o tipo de transporte:', options=listaTransportes,index=0)
    filter3= st.selectbox('Selecione o tipo de visualização:', options=["quantidade","porcentagem"],index=0)



dfFiltrado=dfTotal.loc[ (dfTotal["trajeto"].isin(filter1)) & (dfTotal["transporte"]==filter2) ][filter3]
valor=list(dfFiltrado)

if filter3=="porcentagem":
    suffixo='%'
else:
    suffixo=''

try:
    print("OKKKKK")
except:
    print('Indice fora do limite')
    valor.append(0)



Indicador=Figure(Indicator(
mode="gauge+number",
value=valor[0],
number={'suffix':suffixo},
domain ={'x': [0, 1], 'y': [0, 1]},
gauge={'bar':{'color':'crimson'}}
))
Indicador.update_layout(
    height=250,
    width=50,
    margin=dict(l=0,r=0,t=0,b=0)
    )

with col2:
    st.plotly_chart(Indicador)