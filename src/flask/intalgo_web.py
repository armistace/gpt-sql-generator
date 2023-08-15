import modeller.dbt_docker as dbt
from open_ai.open_ai import dbt_builder as ai_dbt
from open_ai.get_sources import Sources_Generator as source_gen
import logging

from flask import Flask, render_template, request, session
from markupsafe import Markup, escape
import re
import os


log = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)



app = Flask(__name__)
# Set up for sessions with secret key
app.secret_key = os.getenv('SESSION_SECRET_KEY')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dbt_ai', methods=["GET", "POST"])
def get_ai_results():
    #TODO: set up template renderer and workout how to 
    #      get the same thing ot work over nad over
    if request.method == "POST":
        ai_instance = ai_dbt(log)
        user_query = request.form["query"]
        ai_instance.set_query(user_query)
        ai_instance.query_openai()
        ai_instance.write_to_dbt()
        # Add current query sql file to session so we can retrieve to return results
        session['current_query'] = ai_instance.get_outfile()
        log.info(f"Setting Current Query: {ai_instance.get_outfile()}")

        return render_template("query.html", query=ai_instance.show_query())
    else:
        return render_template("ai_query.html")

@app.route('/debug')
def show_debug():
    dbt_run = dbt.docker_dbt()
    output = dbt_run.dbt_debug("ls /intalgo/src/dbt")
    log.info(output)
    return render_template('logs.html', logs=output)


@app.route('/results')
def show_results():
    # Get that query file    
    query = session['current_query']
    # Clean up our session storage
    session.pop('current_query', default=None)
    log.info(f"Retrieved Current Query {query}")

    dbt_run = dbt.docker_dbt()
    output = dbt_run.show_dbt_results(query)
    log.info(output)
    return render_template('show.html', results=output)

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

@app.route('/connect_source', methods=["GET", "POST"])
def build_sources():
    source = source_gen(log)
    if request.method == "POST":
        source_type = request.form["source_type"]
        source.get_example_yaml(source_type)
        return render_template("show_example.html", example_yaml=source.html_render_yaml())
    else:
        return render_template("source_list.html", source_list=source.example_list)


if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
