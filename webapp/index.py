from flask import Flask, Response
from flask import render_template, url_for

from load_csv import export_gastos

import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/data/<int:year>/<int:month>")
def data(year, month):
    data = json.dumps(export_gastos(year, month))
    return Response(data, mimetype='text/json')

@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)
