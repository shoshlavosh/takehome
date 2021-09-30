from flask import (Flask, render_template, request, flash, session, redirect, jsonify)
#render_template is called on the Jinja template, 
#Flask will return it to the browser 

from model import connect_to_db
import crud

from datetime import datetime

from jinja2 import StrictUndefined #shows errors if there's an undefined variable

app = Flask(__name__) #new instance of Flask class assigned to app variable
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route("/")
def index():
    """Show homepage"""

    return render_template("index.html") 
    #function renders this template, 
    #returns this route as html to the browser
    #Flask is exposing this route to the internet



@app.route("/login", methods=['POST'])
def handle_login():
    """Log user in"""

    email = request.form['email'] 
    password = request.form['password']

    user = crud.get_user_by_email(email)

    if not user:
        flash("Error: This user does not exist.")
        flash("Please create an account below.")
        return redirect("/")

    if user.password != password:
        flash("Error: wrong password.")
        return redirect("/") #redirects to homepage
    
    else:
        session['user_email'] = user.email #adds key to Flask session
        flash(f'Logged in. Welcome back, {user.email}!')
        return redirect("/search")



if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')