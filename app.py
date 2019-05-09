# imports go here.
from flask import Flask , request

app = Flask(__name__)

### Routes ####
## these functions dictate how your server responds to HTTP requests.
## Request object docs: http://flask.pocoo.org/docs/1.0/api/#flask.Request
@app.route("/", methods=["GET"])
def index():
    return "Hello, world!"

# /login?username=x&password=1

@app.route('/login', methods=['GET'])
def login():
	##data = request.args.get('username','password' )
	##print(data)
   username = request.args.get('username')
#  print(data['username'])
   password= request.args.get('password')
 #   print(data['password'])
   return username + password

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(username)

# This block is run if you execute this file locally, i.e. running 
# `python3 app.py` from the command line. You can change the port if you want.
# if you're curious: 
# __name__ is a magic variable set by the python interpreter upon executing this file. 
# more info: https://stackoverflow.com/a/419185
if __name__ == "__main__":
    app.run(port=5050)