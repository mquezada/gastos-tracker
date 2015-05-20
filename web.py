from flask import Flask, Response
from flask import render_template, url_for
import json

from web import load_csv 
from src.create_session import session
from src.model import Expense, Category 
from src.methods import *

app = Flask(__name__, template_folder="web/templates/", static_folder="web/static/")


@app.route("/")
def index():
    dates = get_dates_comparison()
    this_month = get_expenses_month(dates[0], dates[1])
    prev_month = get_expenses_month(dates[2], dates[3])
    
    s_t = get_total(this_month)
    s_p = get_total(prev_month)
    
    return render_template('index.html', this_month=s_t, prev_month=s_p)


@app.route("/data/<int:year>/<int:month>")
def data(year, month):
    data = json.dumps(load_csv.export_gastos(year, month))
    return Response(data, mimetype='text/json')


@app.route('/<path:path>')
def static_proxy(path):
  # send_static_file will guess the correct MIME type
  return app.send_static_file(path)


if __name__ == "__main__":
    app.run(debug=True)
