import modeller.dbt_docker as dbt
import logging

from flask import Flask, render_template
from markupsafe import Markup, escape
import re


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



app = Flask(__name__)

@app.route('/')
def run_dbt_test():
    dbt_test = dbt.docker_dbt()
    cont_logs = dbt_test.run_dbt_test()
    #docker returns a byte array this maps it to make it readable
    output = Markup("<br>".join(re.split(r'(?:\r\n|\r|\n)', escape(''.join(map(chr, cont_logs))))))

    log.info(output)
    return render_template('logs.html', logs=output)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
