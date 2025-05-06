from flask import Blueprint
import pandas as pd
from plotly.express import scatter_map
from plotly.io import to_json,write_image
from models import db

trecho_blueprint = Blueprint('trecho', __name__)


@trecho_blueprint.route('/trecho', methods=['GET'])
def read_trecho():
    engine = db.get_engine()

    df=pd.read_sql('select * from trecho', engine)
    df["cidade"]=df["cidade"].str.lower().str.capitalize().str.strip()


    map=scatter_map(df, lat='latitude', lon='longitude',color='cidade', hover_name='cidade',map_style="dark",width=600,height=250)
    map.update_traces(marker={'size':15})  #seta o tamanho dos pontos no mapa

    map.update_layout(margin= { "r":0,"t":0,"b":0,"l":0},legend_title="cidade")
    mapJson=to_json(map,pretty=True)

    #write_image(map, 'frontend/app/src/map.png')

    return mapJson