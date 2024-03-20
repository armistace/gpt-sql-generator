import os
import openai
import requests
import re
from datetime import datetime
from markupsafe import Markup, escape


openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-OzlolStjF4eoUeYq6meETBmQ"

class Sources_Generator:
    def __init__(self, log):
        self.log = log
        self.sources = self.sources_json()
        self.example_list = self.source_list()
        self.dbt_source = '/root/.dbt/example/'
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        self.outfile = "sources_" + timestamp + ".yml"

    def query_openai(self):
        gpt_question = f"generate a yml file using the following example yaml as a reference: \n```\n{self.example_yaml}\n```\n replace the right keys with the following information: {self.query}. Only output the yaml"
        self.log.info(gpt_question)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": gpt_question},
            ], max_tokens=1000)

        self.response = response
        self.yaml = self.response["choices"][0]["message"]["content"]

        #dbt_gpt = 

    def set_query(self, query):
        self.query =  query

    def sources_json(self):
        self.sources_url = "https://github.com/datahub-project/datahub/tree/master/metadata-ingestion/docs/sources"
        sources = requests.get(self.sources_url)
        self.log.info(sources)
        return sources


    def source_list(self):
        return_list = []

        for name in self.sources.json()["payload"]["tree"]["items"]:
            return_list.append(name["name"])

        return return_list

    def get_example_yaml(self, source_type):
        yaml_file = ""
        for item in self.sources.json()["payload"]["tree"]["items"]:
            if item["name"] == source_type:
                recipe_finder = requests.get(f'{self.sources_url}/{item["name"]}')
                for finder in recipe_finder.json()["payload"]["tree"]["items"]:
                    if finder["name"][-4:] == ".yml":
                        recipe_url = f'{self.sources_url}/{item["name"]}/{finder["name"]}'
                        yaml = requests.get(recipe_url)
                        for line in yaml.json()["payload"]["blob"]["rawLines"]:
                            yaml_file = f"{yaml_file} \n {line}"
                dbt_profile = f'{self.dbt_profile}/{item["name"]}.yml'
        self.log.info(yaml_file)
        self.example_yaml = yaml_file

    def html_render_yaml(self, yaml_render):
        return Markup("<br>".join(re.split(r'(?:\r\n|\r|\n)', \
                escape(''.join( yaml_render)))))

    def output_file(self):
        with open (f"src/datahub/{self.outfile}", "w") as out_file:
            for line in self.response.choices:
                self.log.info(line['message']['content'])
                out_file.write(line['message']['content'])



