# imports go here.
from flask import Flask

app = Flask(__name__)

### Routes ####
## these functions dictate how your server responds to HTTP requests.
## Request object docs: http://flask.pocoo.org/docs/1.0/api/#flask.Request
@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"


@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

# This block is run if you execute this file locally, i.e. running 
# `python3 app.py` from the command line. You can change the port if you want.
# if you're curious: 
# __name__ is a magic variable set by the python interpreter upon executing this file. 
# more info: https://stackoverflow.com/a/419185
if __name__ == "__main__":
    app.run(port=5050)