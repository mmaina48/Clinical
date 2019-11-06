from flask import Flask ,render_template

app=Flask(__name__)
app.secret_key='maich key'

@app.route('/',methods=['GET', 'POST'])
def login():
 
    return render_template("home.html")

if __name__=="__main__":
    app.run(debug=True)