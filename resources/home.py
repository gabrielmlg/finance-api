from flask_restful import Resource

class Home(Resource):
    def get(self):
        return {'message': 'Meus investimentos ...'}
    def post(self):
        return {'message': 'Meus investimentos ...'}