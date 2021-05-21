import flask
from flask import render_template, request

app = flask.Flask(__name__)

@app.route("/")
def root():
  return render_template("index.html")

@app.route("/testing")
def testing():
  return render_template("testing.html")

@app.route("/form")
def form():
  return render_template("form.html")


@app.route("/calculate")
def calculate():
  output = "Mark 1: " + request.args["mark1"] + ", weightage 1: " + request.args["weightage1"] + "<br>"
  output += "Mark 2: " + request.args["mark2"] + ", weightage 2: " + request.args["weightage2"] + "<br>"
  output += "Mark 3: " + request.args["mark3"] + ", weightage 3: " + request.args["weightage3"] + "<br>"
  return output

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0", port=8080, debug=True)
