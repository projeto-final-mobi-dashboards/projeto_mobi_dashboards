from flask import Blueprint
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plotly.io import to_json
from models import db
import mysql.connector as sql



transport_blueprint = Blueprint('transport', __name__)

@transport_blueprint.route('/transport', methods=['GET'])
def transport():
    engine = db.get_engine()


    dfTransporteIda=pd.read_sql('select trecho.meio_transporte from trecho,itinerario,usuarios where trecho.itinerario_id=itinerario.id and itinerario.usuario_id=usuarios.id and trecho.tipo_trajeto="volta";', engine)

    dfTransporteVolta=pd.read_sql('select trecho.meio_transporte from trecho,itinerario,usuarios where trecho.itinerario_id=itinerario.id and itinerario.usuario_id=usuarios.id and trecho.tipo_trajeto="volta";', engine)


    dfTransporteIda=dfTransporteIda.groupby(by=['meio_transporte']).value_counts().reset_index()
    dfTransporteIda.columns=['meio_transporte','quantidade']
    dfTransporteIda["porcentagem"]=100*(dfTransporteIda['quantidade']/(dfTransporteIda['quantidade'].sum()))
    dfTransporteIda["porcentagem"]=dfTransporteIda["porcentagem"].round(2).astype('string')+'%'


    dfTransporteVolta=dfTransporteVolta.groupby(by=['meio_transporte']).value_counts().reset_index()
    dfTransporteVolta.columns=['meio_transporte','quantidade']
    dfTransporteVolta["porcentagem"]=100*(dfTransporteVolta['quantidade']/(dfTransporteVolta['quantidade'].sum()))
    dfTransporteVolta["porcentagem"]=dfTransporteVolta["porcentagem"].round(2).astype('string')+'%'


    tabelaIda= go.Table(
                                header=dict
                                (
                                    values=list(dfTransporteIda.columns),
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    align='center'
                                ),
                                cells=dict(
                                        values=
                                        [
                                            dfTransporteIda.meio_transporte,
                                            dfTransporteIda.quantidade,
                                            dfTransporteIda.porcentagem
                                        ],
                                        fill_color='lavender',
                                        align='center',
                                ))

    tabelaVolta= go.Table(      
                                header=dict
                                (
                                    values=list(dfTransporteVolta.columns),
                                    line_color='darkslategray',
                                    fill_color='lightskyblue',
                                    align='center',
                                ),
                                cells=dict(
                                        values=
                                        [
                                            dfTransporteVolta.meio_transporte,
                                            dfTransporteVolta.quantidade,
                                            dfTransporteVolta.porcentagem
                                        ],
                                        fill_color='lavender',
                                        align='center'))



    tabelasUnidas = make_subplots(
                                    rows=1,
                                    cols=2,
                                    specs=[[{"type":"table"},{"type":"table"}]],
                                    subplot_titles=("Tabela Ida", "Tabela Volta"),
                                    horizontal_spacing=0,
                                    column_widths=[1,1]
                                )

    tabelasUnidas.add_trace(tabelaIda, row=1,col=1 )
    tabelasUnidas.add_trace(tabelaVolta, row=1,col=2 )
    tabelasUnidas.update_layout( shapes=[dict(type="line",x0=0.5,y0=1, x1=0.5,y1=1 , line=dict(color="black",width=2))] )

    return to_json(tabelasUnidas,pretty=True)
#   return coisa