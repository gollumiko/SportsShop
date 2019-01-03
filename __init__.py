from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def home():
    return ":D"

if __name__ == "__main__":
    app.run()