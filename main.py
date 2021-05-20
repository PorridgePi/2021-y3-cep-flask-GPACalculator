import flask
from flask import render_template

app = flask.Flask(__name__)

@app.route("/")
def root():
  return render_template("index.html")

@app.route("/testing")
def testing():
  return render_template("testing.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0", port=8080, debug=True)
