import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-OzlolStjF4eoUeYq6meETBmQ"

class dbt_builder:
    def __init__(self, log):
        with open ('src/dbt/intalgo/models/sources.yml', 'r') as source_file:
            sources = source_file.read()

        self.sources_prompt = f"Using the input dbt sources yaml of {sources} Generate DBT compliant sql without wrapping it triple quotes that answers the question "
        self.log = log
        self.remove_semicolon = f" just show the sql without the semi colon at the end of the query. Make sure to reference the sources correctly"
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.outfile = "query_" + timestamp + ".sql"

    def set_query(self, query):

        self.query = query

    def get_outfile(self):

        return self.outfile

    def query_openai(self):
        self.response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": f"{self.sources_prompt}{self.query}{self.remove_semicolon}"},
        ], max_tokens=1000)



    def write_to_dbt(self):
        with open (f"src/dbt/intalgo/models/ai_query/{self.outfile}", "w") as out_file:
            self.log.info(f"Output writing to {self.outfile}")
            for line in self.response.choices:
                self.log.info(line['message']['content'])
                out_file.write(line['message']['content'])

    def show_query(self):
        string = ""
        f = open (f"src/dbt/intalgo/models/ai_query/{self.outfile}", "r")
        in_file = f.readlines()
        for line in in_file:
            string = f"{string} {line} \n"
        return string
