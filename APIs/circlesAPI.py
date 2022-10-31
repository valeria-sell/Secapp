from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
    def get(self):
        return {'about':'Hello!'}

class AddFriend(Resource):
    def get(self):
        return {'about':'Aqui agrego amigos!'}
    def post(self):
        #nota: aqui deberia jalar los datos de Thunkable para publicar
        some_json = request.get_json()
        return {'you added a friend': some_json}, 201

class CreateCircle(Resource):
    def get(self):
        return {'about':'Aqui creo circulos!'}
    def post(self):
        #nota: aqui deberia jalar los datos de Thunkable para publicar
        some_json = request.get_json()
        return {'you created a circle': some_json}, 201

class AddtoCircle(Resource):
    def get(self):
        return {'about':'Aqui agrego amigos a los circulos!'}
    def post(self):
        #nota: aqui deberia jalar los datos de Thunkable para publicar
        some_json = request.get_json()
        return {'you added to circle': some_json}, 201

api.add_resource(Home, '/')
api.add_resource(AddFriend, '/addFriend')
api.add_resource(CreateCircle, '/createCircle')
api.add_resource(AddtoCircle, '/addtoCircle')

if __name__ == '__main__':
    app.run(debug=True)