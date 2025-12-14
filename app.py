from flask import Flask, render_template, request

app = Flask(__name__)

support_programs = [
    {
        "name": "재난적 의료비 지원",
        "income_max": 3,
        "disease": ["암", "중증질환"]
    },
    {
        "name": "희귀질환 의료비 지원",
        "income_max": 2,
        "disease": ["희귀질환"]
    }
]

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
    income = int(request.form["income"])
    disease = request.form["disease"]

    result = []
    for p in support_programs:
        if income <= p["income_max"] and disease in p["disease"]:
            result.append(p["name"])

    return render_template("result.html", result=result)

app.run()
