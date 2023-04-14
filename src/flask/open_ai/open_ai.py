import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

class dbt_builder:
    def __init__(self):
        with open ('src/dbt/intalgo/models/sources.yml', 'r') as source_file:
            sources = source_file.read() 
        
        self.sources_prompt = f"Using the input dbt sources yaml of {sources} Generate a DBT compliant sql file that answers the question "


    def get_query(self, query):

        self.query = query
    
    def query_openai(self):
        self.response = openai.Completion.create(model="text-davinci-003", prompt=f"{self.sources_prompt}{self.query}", max_tokens=100)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.outfile = "query_" + timestamp + ".sql"

    def write_to_dbt(self):
        with open (f"src/dbt/intalgo/models/ai_query/{self.outfile}", "a") as out_file:

            for line in self.response.choices:
    
                out_file.write(line.text)
       
    def show_query(self):
        string = ""
        f = open (f"src/dbt/intalgo/models/ai_query/{self.outfile}", "r")
        in_file = f.readlines()
        for line in in_file:
            string = f"{string} {line} \n"
        return string
