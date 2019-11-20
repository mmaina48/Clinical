from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, login_user, current_user, login_required , logout_user
from passlib.hash import pbkdf2_sha256
from wtform_fields import *
from models import *

#config app 
app=Flask(__name__)
app.secret_key='maich key'


#configure database

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hohloipsofwxru:c3f564adeb73ca6bf766d4bb9120f082f3ba50cd5812335a3e32a37991d040f4@ec2-174-129-210-249.compute-1.amazonaws.com:5432/dfp379s14ksj67'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

#configuring flask login
login= LoginManager(app)
login.init_app(app)

@login.user_loader
def load_user(id):

     return User.query.get(int(id))

@app.route('/', methods=['GET', 'POST'])
def reg():

    reg_form = RegistrationForm()
#update database if validation sucessfull
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data

        # hashed password
        hashed_passwd=pbkdf2_sha256.hash(password)


        user = User(username=username, password=hashed_passwd)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('login'))        

    return render_template("home.html", form=reg_form)

@app.route("/login", methods=['GET','POST'])
def login():
    #initatiate
    loginform = LoginForm()

    #allow login if no validation error
    if loginform.validate_on_submit():
        user_object = User.query.filter_by(username=loginform.username.data).first()
        login_user(user_object)
        return redirect(url_for('chat'))
        

    return render_template("login.html", form=loginform)

@app.route("/chat", methods=['GET','POST'])
def chat():

    if not current_user.is_authenticated:
        return redirect(url_for('login'))

    return " chat PAGE"

@app.route("/logout", methods=['GET'])
def logout():

    logout_user()
    return "Logout using flask-login"



if __name__ == "__main__":
    app.run(debug=True)
