########################################################### Blueprints
from blueprints.usergenderBar import genderBlueprint
from blueprints.indicatorTransport import transportBlueprint
from blueprints.mapRoute import mapBlueprint
from blueprints.pieChartRoute import adressesBlueprint
from blueprints.cursosColunas import cursoBlueprint
from blueprints.sent_event import sent_eventBlueprint
from flask import Flask

def register_Blueprints(app: Flask):
    app.register_blueprint(cursoBlueprint)
    app.register_blueprint(adressesBlueprint)
    app.register_blueprint(mapBlueprint)
    app.register_blueprint(genderBlueprint)
    app.register_blueprint(transportBlueprint)
    app.register_blueprint(sent_eventBlueprint)
    return None
