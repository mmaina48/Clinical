from flask import Flask ,render_template
from wtform_fields import *

#config app 
app=Flask(__name__)
app.secret_key='maich key'

@app.route('/',methods=['GET', 'POST'])
def reg():

    reg_form=RegistrationForm()
    if reg_form.validate_on_submit():
        return "Great Sucess!"

    return render_template("home.html", form=reg_form)

if __name__=="__main__":
    app.run(debug=True)
