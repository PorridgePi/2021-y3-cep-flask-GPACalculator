import flask
from flask import render_template, request

app = flask.Flask(__name__)

global numItems
numItems = 3

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
    data = request.form
    
    totalWeightage = 0
    rawPercentage = 0

    for i in range(len(data) // 2):
        mark = data[f"mark{i}"]
        weightage = data[f"weightage{i}"]
        if weightage.isdigit() and mark.isdigit():
            totalWeightage += int(weightage)
    
    for i in range(len(data) // 2):
        mark = data[f"mark{i}"]
        weightage = data[f"weightage{i}"]
        if weightage.isdigit() and mark.isdigit():
            if int(mark) > 100:
                return render_template("error.html", error="Mark must not higher than 100.")
            rawPercentage += int(mark)*int(weightage)

    rawPercentage /= totalWeightage

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

    return render_template("result.html", form=request.form, percentage=totalPercentage, grade=grade)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

app.run(host="0.0.0.0", port=8080, debug=True)
