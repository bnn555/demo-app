from flask import Flask, request
import os

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World from Nicolae demo app!</p>"


if __name__ == "__main__":
    port = int(os.environ.get('APP_PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)