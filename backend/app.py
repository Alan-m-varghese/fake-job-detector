from flask import Flask, render_template, request
from fake_detector import detect_fake

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        job_text = request.form["job_text"]
        result = detect_fake(job_text)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
