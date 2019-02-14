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
@app.route('/log', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form['password']
        user = session.query(User).filter_by(name=name).first()
        if user is not None:
            #user = session.query(User).filter_by(name=name)
            if user.password ==password:
                return render_template('home.html',user=user)
        else:
            flash("not such user in db")
            return redirect(url_for('log'))       
    else:
         return render_template('log.html')
@app.route('/home')
def home():
    return render_template('Home.html')

    
@app.route('/reg', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def reg():
      if request.method == 'POST':
          user1 = User(name=request.form['name'],
                      password = request.form['password'])
          session.add(user1)
          session.commit()
          flash("sccussfully signing in ...")
          return render_template('Home.html',user = user1)
      else:
          return render_template('register.html')
        
      

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'Sakr_Secret_Key'
    app.run()