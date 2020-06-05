from flask_restful import Resource

class Fundo(Resource):
    def get(self):
        return { 
            'status': 'success', 
            'data': 'TESTE'
        }, 200