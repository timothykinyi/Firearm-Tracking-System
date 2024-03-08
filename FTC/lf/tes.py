from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/police")
def get_police_data():
    data = getpoliceinfo()
    return 