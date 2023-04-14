import modeller.dbt_docker as dbt
from open_ai.open_ai import dbt_builder as ai_dbt
import logging

from flask import Flask, render_template, request
from markupsafe import Markup, escape
import re


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dbt_ai', methods=["GET", "POST"])
def get_ai_results():
    #TODO: set up template renderer and workout how to 
    #      get the same thing ot work over nad over
    if request.method == "POST":
        ai_instance = ai_dbt()
        user_query = request.form["query"]
        ai_instance.get_query(user_query)
        ai_instance.query_openai()
        ai_instance.write_to_dbt()
        return render_template("query.html", query=ai_instance.show_query())
    else:
        return render_template("ai_query.html")

@app.route('/run')
def run_full_dbt():
    dbt_run = dbt.docker_dbt()
    output = dbt_run.run_full_dbt()
    log.info(output)
    return render_template('logs.html', logs=output)

@app.route('/test')
def run_dbt_test():
    dbt_test = dbt.docker_dbt()
    output = dbt_test.run_dbt_test()
    log.info(output)
    return render_template('logs.html', logs=output)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
