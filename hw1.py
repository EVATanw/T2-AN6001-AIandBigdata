from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def HWagenda():
    return(render_template("HWagenda.html"))

@app.route("/HWq1", methods=["GET", "POST"])
def HWq1():
    return render_template("HWq1.html")

if __name__ == "__main__":
    app.run()




