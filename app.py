from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
import json

app = Flask(__name__)


MONGO_URI = "mongodb+srv://admin:KxUPQazXf3tl7nI6@cluster0.rtfzu8v.mongodb.net/?appName=Cluster0"
client = MongoClient(MONGO_URI)

db = client["flaskDB"]
collection = db["users"]

@app.route("/api")
def api():
    with open("data.json", "r") as file:
        data = json.load(file)
    return jsonify(data)

@app.route("/", methods=["GET", "POST"])
def form():
    error = None
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]

            collection.insert_one({
                "name": name,
                "email": email
            })

            return redirect(url_for("success"))
        except Exception as e:
            error = str(e)

    return render_template("form.html", error=error)

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)
