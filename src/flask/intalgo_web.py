import modeller.dbt_docker as dbt

from flask import Flask


app = Flask(__name__)

@app.route('/')
def run_dbt_test():
    dbt_test = dbt.docker_dbt()
    output = dbt_test.run_dbt_test()
    return output

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
