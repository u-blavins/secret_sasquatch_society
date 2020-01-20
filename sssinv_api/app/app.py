from db import Database
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
mydb = Database(
    'DRIVER',
    'ENDPOINT',
    'User',
    'User',
    'Password'
)
users = []

@app.route('/')
@app.route('/auth')
def auth():
    return render_template('auth.html')

@app.route('/auth/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        args = {
            'fname': request.form['fname'],
            'lname': request.form['lname'],
            'email': request.form['email'],
            'pass': request.form['pass'],
            'deptcode': request.form['deptcode']
        }
        return mydb.register_user(args)
        if request.form['conpass'] == args['pass']:
            users.append(args)
            return render_template('auth.html')

@app.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        args = {
            'email': request.form['email'],
            'pass': request.form['pass']
        }
        # return mydb.login_user(args)
        return render_template('index.html')
    return render_template('auth.html')

if __name__ == '__main__':
    app.run(host='localhost', port=5005, debug=True)