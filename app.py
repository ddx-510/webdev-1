from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
app.config["DEBUG"] = True

user_comments = {}

@app.route("/", methods=[     ,      ])  # hint: what is the methods we may use to differentiate two status?

def index():
    if request.method == "   ":  # hint: what if the user does not click the post button?
        return render_template("", user_comments=user_comments)  # hint:what is the name for your main page?
    else: # post
        user_comments[request.form["uname"]] = request.form["contents"]
        return redirect(                )   # hint: if we want to go back to index function, what should we do inside the redirect?


# This block is run if you execute this file locally, i.e. running 
# `python3 app.py` from the command line. You can change the port if you want.
# if you're curious: 
# __name__ is a magic variable set by the python interpreter upon executing this file. 
# more info: https://stackoverflow.com/a/419185
if __name__ == "__main__":
    app.run(port=5050)
