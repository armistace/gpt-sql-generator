import modeller.dbt_docker as dbt
import logging

from flask import Flask, render_template
from markupsafe import Markup, escape
import re


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
