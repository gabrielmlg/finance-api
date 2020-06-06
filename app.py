from flask import Blueprint
from flask_restful import Api
from resources.home import Home
from resources.fi import Fundo
from resources.posicao import Posicao

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Route
api.add_resource(Home, '/home')
api.add_resource(Fundo, '/fi')
api.add_resource(Posicao, '/posicao')

