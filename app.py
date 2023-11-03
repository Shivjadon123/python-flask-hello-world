from flask import Flask
from weasyprint import HTML
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"
