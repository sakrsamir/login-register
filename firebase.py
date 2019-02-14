import pyrebase
from flask import Flask, render_template, url_for, request, redirect, flash, jsonify, make_response
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

app = Flask(__name__)



#  Routing
@app.route('/', methods=['GET', 'POST'])
def log():
    if request.method == 'POST':
        name = request.form['user']
        password = request.form['password']
        db.child("users").push({"name" : name,"pass" : password})
        tes = db.child("users").get()
        t = tes.val()
        m = t.values()
        flash('logged in as %s !' %m)
        return render_template('Home.html')
    else:
         return render_template('login.html')

    

if __name__ == '__main__':
    app.debug = True
    app.secret_key = 'Sakr_Secret_Key'
    app.run()