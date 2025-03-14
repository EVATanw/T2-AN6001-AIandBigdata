from flask import Flask
from flask import render_template,request
from textblob import TextBlob
import os
import google.generativeai as genai

api = os.getenv("makersuite")
genai.configure(api_key="api")
model = genai.GenerativeModel('gemini-1.5-flash') #github 本地无法运行，因为没有apikey，在render里面给了apikey所以可以
#test
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    name = request.form.get("q")
    return(render_template("main.html"))

@app.route("/SA",methods=["GET","POST"])
def SA():
    return(render_template("SA.html"))

@app.route("/SA_result",methods=["GET","POST"])
def SA_result():
    q = request.form.get("q")
    r = TextBlob(q).sentiment
    return(render_template("SA_result.html",r=r))

@app.route("/genAI",methods=["GET","POST"])
def genAI():
    return(render_template("genAI.html"))

@app.route("/genAI_result",methods=["GET","POST"])
def genAI_result():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("genAI_result.html",r=r.candidates[0].content.parts[0].text))

@app.route("/paynow",methods=["GET","POST"])
def paynow():
    return(render_template("paynow.html"))

if __name__ == "__main__":
    app.run()




