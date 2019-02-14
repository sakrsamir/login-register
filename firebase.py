#import pyrebase
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_setup import Base, User
'''
# using firebase realtime database#
config = {
    "apiKey": "AIzaSyB1lQm44bKt5dfC1mZXPedn-5NzC6wTSPU",
    "authDomain": "stock-6b194.firebaseapp.com",
    "databaseURL": "https://stock-6b194.firebaseio.com",
    "projectId": "stock-6b194",
    "storageBucket": "stock-6b194.appspot.com",
    "messagingSenderId": "653335079989"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
'''
app = Flask(__name__)

engine = create_engine('sqlite:///users.db')
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)
session = DBSession()

#  Routing
@app.route('/login', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form['password']
    else:
         return render_template('login.html')
@app.route('/')
def home():
    user = session.query(User).first()
    return user.name 
    

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'Sakr_Secret_Key'
    app.run()