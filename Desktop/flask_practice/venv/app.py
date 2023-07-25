from flask import Flask,request,render_template
app = Flask(__name__)
@app.route("/")
def welcome():
    return render_template("form.html")
@app.route("/form_submission")
def submit():
    print(request.args)
    req_args = request.args
    Username = req_args.get("uname")
    password= req_args.get("psw")
    return render_template("data.html",username=Username)
    #return req_args