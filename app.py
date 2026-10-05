from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return {"message": "Hello OpenTelemetry"}

if __name__ == "__main__":
    app.run(port=8080)