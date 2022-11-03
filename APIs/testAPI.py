from flask import Flask, request
from flask_restful import Resource, Api
from firebase_admin import credentials, initialize_app

cred = credentials.Certificate("APIs/key.json") 
default_app = initialize_app(cred) # si no funciona, probar con (cred, {"databaseURL": "https://secapp-bdii-default-rtdb.firebaseio.com")})

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

test1 = {
"userID":[
    {"latitude":"1.442353", "longitude":"174.117", "dangerType": "Carro sospechoso", "timeAndDate": "2022-11-01 10:34:23", 
    "message":"Carro detenenido con vidrios polarizados. Placa 763846.", "typedLocation":"Frente a escuela Sony"},
]}

newfrienddata = {
"2ut4hpMzQYRz9S3ivSWoQRwaxvs1":   
    { 
    "friends":[
        {"email":"Anna123@gmail.com", "userID": "Jo3eWPJdntZsrE0N5FUkXePRMFz1"}]
    } 
}

class AddDanger(Resource):
    def get(self):
        return {'about':'Aqui agrego amigos a los circulos!'}
    def post(self):
        #nota: aqui deberia jalar los datos de Thunkable para publicar
        return {'you added danger': test2}, 201
 
api.add_resource(Home, '/')
api.add_resource(AddFriend, '/addFriend')
api.add_resource(CreateCircle, '/createCircle')
api.add_resource(AddtoCircle, '/addtoCircle')
api.add_resource(AddDanger, '/addDanger')

if __name__ == '__main__':
    app.run(debug=True)