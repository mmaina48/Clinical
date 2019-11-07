from flask import Flask ,render_template
from wtform_fields import *
from models import *

#config app 
app=Flask(__name__)
app.secret_key='maich key'


#configure database

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hohloipsofwxru:c3f564adeb73ca6bf766d4bb9120f082f3ba50cd5812335a3e32a37991d040f4@ec2-174-129-210-249.compute-1.amazonaws.com:5432/dfp379s14ksj67'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

@app.route('/',methods=['GET', 'POST'])
def reg():

    reg_form=RegistrationForm()
    if reg_form.validate_on_submit():
        username = reg_form.username.data
        password = reg_form.password.data


        #check username is unique
        user_object= User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"

        user= User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return "Inserted to db"            

    return render_template("home.html", form=reg_form)


if __name__=="__main__":
    app.run(debug=True)
