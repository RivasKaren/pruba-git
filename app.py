from flask import Flask

nombre = "Karen"

app = Flask("app_conflicto")

@app.route('/')
def index():
    return f"<h1>Cambio en feature-api</h1>"

@app.route('/api/status')
def status():
    return {"status": "ok"}
print('conflicto feature')
