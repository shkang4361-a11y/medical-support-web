from flask import Flask, render_template, request

app = Flask(__name__)

# 의료비 지원 제도 데이터 (예시)
support_programs = [
    {
        "name": "재난적 의료비 지원",
        "income_max": 3,  # 중위소득 150% 이하
        "disease": ["암", "중증질환"]
    },
    {
        "name": "희귀질환 의료비 지원",
        "income_max": 2,  # 중위소득 120% 이하
        "disease": ["희귀질환"]
    }
]

# 첫 화면
@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")

# 결과 처리
@app.route("/result", methods=["POST"])
def result():
    income = int(request.form["income"])
    disease = request.form["disease"]

    matched = []

    for p in support_programs:
        if income <= p["income_max"] and disease in p["disease"]:
            matched.append(p["name"])

    return render_template("result.html", result=matched)

# ⚠️ 배포 필수 구조
if __name__ == "__main__":
    app.run()
