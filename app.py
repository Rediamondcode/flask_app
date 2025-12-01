from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    message = f"Hello, {name}! Your demo Python app is running successfully."
    return message

if __name__ == "__main__":
    app.run(debug=True)
