from flask import Blueprint
import pandas as pd
from plotly.express import bar
from plotly.io import to_json
from models import db
curso_blueprint = Blueprint('curso', __name__)

@curso_blueprint.route('/cursos', methods=['GET'])
def read():
    engine = db.get_engine()
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
    bars=bar(df_curso,x='curso', y='quantidade', color='quantidade',color_continuous_scale='ice')
    bars.update_layout(xaxis_title="cursos do cefet" , yaxis_title="quantidade de alunos")

    barsJson=to_json(bars, pretty=True)

    return barsJson