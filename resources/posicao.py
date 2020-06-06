from flask_restful import Resource
from classes.repository import PosicaoRepository

class Posicao(Resource):
    def get(self):
        posicao_repository = PosicaoRepository()
        posicao_repository.load_data()
        df_fis = posicao_repository.fis

        print(df_fis.head())

        return { 
            'status': 'success', 
            'data': 'TESTE POSICAO'
        }, 200



