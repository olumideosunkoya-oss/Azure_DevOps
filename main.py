from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python"
@app.route("/add")
def add_user():
    return "added a new user"


if __name__ == "__main__":
    app.run(debug=True)