from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Hello, Chuks!</p>"


if __name__ == '__main__':
  app.run(host= '0.0.0.0', debug = True)