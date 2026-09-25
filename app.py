from flask import Flask

nombre = "Karen"

app = Flask(__name__)

@app.route('/')
def index():
    return f"<h1>Cambio en main</h1>"
