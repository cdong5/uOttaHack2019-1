from flask import *
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
def signin():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['pass']

        user = auth.create_user_with_email_and_password(email, password)
        auth.send_email_verification(user['idToken'])

    return render_template('classify.html')


def login():
    if request.method == 'post':
        unsuccessful = 'The credentials are invalid'
        email_log = request.form['email']
        password_log = request.form['pass']

        try:
            auth.sign_in_with_email_and_password(email_log, password_log)
            return "fuck"
        except:
            return render_template('classify.html', us=unsuccessful)

    return render_template('classify.html')


if __name__ == "__main__":
    app.run(debug=True)
