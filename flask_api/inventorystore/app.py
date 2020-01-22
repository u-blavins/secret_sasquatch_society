from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>')
def greet(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)