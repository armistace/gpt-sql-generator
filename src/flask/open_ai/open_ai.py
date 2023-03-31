import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

class dbt_builder:
    def __init__(self):
        with open ('intalgo/models/sources.yml', 'r') as source_file:
            sources = source_file.read() 
        
        self.sources_prompt = f"Using the input dbt sources yaml of {sources} Generate a DBT compliant sql file that answers the question "


    def get_query(self):
        query = input("ENTER CHATGPT QUERY: ")

        self.query = query
    
    def query_openai(self):
        self.response = openai.Completion.create(model="text-davinci-003", prompt=f"{self.sources_prompt}{self.query}", max_tokens=100)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        self.outfile = "query_" + timestamp + ".sql"

    def write_to_dbt(self):
        with open (f"intalgo/models/ai_query/{outfile}", "a") as out_file:

            for line in response.choices:
    
                self.out_file.write(line.text)
        
