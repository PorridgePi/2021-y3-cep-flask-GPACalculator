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

@app.route("/calculate", methods=["POST"])
def calculate():
    return render_template("result.html", form=request.form)

    mark1, mark2, mark3 = float(request.form["mark1"]), float(request.form["mark2"]), float(request.form["mark3"])

    weightage1, weightage2, weightage3 = float(request.form["weightage1"]), float(request.form["weightage2"]), float(request.form["weightage3"])

    totalWeightage = weightage1 + weightage2 + weightage3

    rawPercentage = (mark1 / 100 / totalWeightage * weightage1 + mark2 / 100 / totalWeightage * weightage2 + mark3 / 100 / totalWeightage * weightage3) * 100

    totalPercentage = round(rawPercentage, 1)

    if totalPercentage >= 80:
        grade = "4.0"
    elif totalPercentage >= 70:
        grade = "3.6"
    elif totalPercentage >= 65:
        grade = "3.2"
    elif totalPercentage >= 60:
        grade = "2.8"
    elif totalPercentage >= 55:
        grade = "2.4"
    elif totalPercentage >= 50:
        grade = "2.0"
    elif totalPercentage >= 45:
        grade = "1.6"
    elif totalPercentage >= 40:
        grade = "1.2"
    else:
        grade = "0.8"

    output = "Mark 1: " + str(mark1) + " Weightage 1: " + str(weightage1) + "<br>"
    output += "Mark 2: " + str(mark2) + " Weightage 2: " + str(weightage2) + "<br>"
    output += "Mark 3: " + str(mark3) + " Weightage 3: " + str(weightage3) + "<br>"

    output += "Percentage: " + str(totalPercentage) + "<br>"
    output += "GPA: " + grade

    return output

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0", port=8080, debug=True)
