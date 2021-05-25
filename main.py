import flask
from flask import render_template, request

app = flask.Flask(__name__)

global numItems
numItems = 5

@app.route("/")
def root():
    return render_template("index.html")

@app.route("/testing")
def testing():
    return render_template("testing.html")

@app.route("/form")
def form():
    return render_template("form.html", numItems = numItems)

@app.route("/calculate", methods=["POST"])
def calculate():
    return render_template("result.html", form=request.form, numItems = numItems)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0", port=8080, debug=True)
