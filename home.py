from flask import*
import pyrebase

app = Flask(__name__)

config = {
    "apiKey": "AIzaSyA4xzA48FI9lGG6mfn5QKnGeUyYlU3FxHM",
    "authDomain": "uottahack-7cb21.firebaseapp.com",
    "databaseURL": "https://uottahack-7cb21.firebaseio.com",
    "projectId": "uottahack-7cb21",
    "storageBucket": "uottahack-7cb21.appspot.com",
    "messagingSenderId": "418633867762"
  };

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

@app.route('/', methods=['GET', 'POST'])

def login():
    if request.method =='POST':
        email = request.form['name']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email, password)
        except:
            'Wrong credentials'

    return render_template('classify.html')

if __name__ == "__main__":
    app.run(debug=True)