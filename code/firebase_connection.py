
from flask import Flask, session, render_template, request, redirect
import pyrebase

app = Flask(__name__)

config= {
  'apiKey': "AIzaSyC1WNSOM4t159pQOqPBJMam_m77KKPiZ5g",
  'authDomain': "secapp-bdii.firebaseapp.com",
  'databaseURL': "https://secapp-bdii-default-rtdb.firebaseio.com",
  'projectId': "secapp-bdii",
  'storageBucket': "secapp-bdii.appspot.com",
  'messagingSenderId': "912547382184",
  'appId': "1:912547382184:web:f1c14ea58c8b0a4516539d",
  'measurementId': "G-2RBVW2DXD0",
  'databaseURL': "" 
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'secret'
#@app.route('/', methods=['POST','GET'])