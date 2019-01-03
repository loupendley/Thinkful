from flask import Flask
app = Flask(__name__)


@app.route("/")  # take note of this decorator syntax, it's a common pattern
def hello():
    return "Wello Harold!, and while we are at it, let's just talk about all of the fun things that we did in 2018.  \"" \
           "Well we did go to the beach, and have a lot of fun, that is for sure."


if __name__ == "__main__":
    app.run(host='0.0.0.0')
