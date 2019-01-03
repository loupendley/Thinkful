from flask import Flask
app = Flask(__name__)


@app.route("/")  # take note of this decorator syntax, it's a common pattern
def hello():
    return "Wello Harold!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
