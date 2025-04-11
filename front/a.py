from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        first = request.form.get("first")
        second = request.form.get("second")

        url = "http://127.0.0.1:5001/getinf"
        data = {"first":first, "second":second}
        response = requests.post(url, json=data)

        response_data = response.json()
        probs = response_data.get("probs")
        pred = response_data.get("pred")
        message = f"{probs}, {pred}"

    return render_template("index.html", message=message)

app.run(host="0.0.0.0", port=5000)
