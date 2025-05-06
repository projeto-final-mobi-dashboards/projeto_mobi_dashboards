from flask import Blueprint
import pandas as pd
from plotly.express import pie
from plotly.io import to_json
from models import db

endereco_blueprint = Blueprint('endereco', __name__)

@endereco_blueprint.route('/endereco', methods=['GET'])
def read_endereco():

    engine = db.get_engine()
    df=pd.read_sql('select * from enderecos', engine)

    PessoasBairro=df['bairro'].value_counts().reset_index()
    pizza = pie(PessoasBairro,values='count', names='bairro',width=500,height=300)
    pizzaJson=to_json(pizza,pretty=True)

    return pizzaJson