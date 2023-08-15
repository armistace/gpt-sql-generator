import os
import openai
import requests
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-OzlolStjF4eoUeYq6meETBmQ"

print(f'API KEY: {os.getenv("OPENAI_API_KEY")}')

def query_openai(query, example_yaml):
    gpt_question = f"generate a yml file using the following example yaml as a reference: \n```\n{example_yaml}\n```\n replace the right keys with the following information: {query}. Only output the yaml"
    print(gpt_question)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": gpt_question},
            ], max_tokens=1000)
    return response

def get_query():
    query = input("Please provide basic information based on example config file above: ")
    return query

def process_response(response):
    return response["choices"][0]["message"]["content"]

def print_result(response):
    print(f"Result")
    print(f"{process_response(response)}")

def get_example_source():
    sources_url = "https://github.com/datahub-project/datahub/tree/master/metadata-ingestion/docs/sources"

    sources = requests.get(sources_url)

    print ("Please Select source from list below: ")
    for name in sources.json()["payload"]["tree"]["items"]:
        print (name["name"])

    source_type = input("Please input source: ")

    yaml_file = ""
    for item in sources.json()["payload"]["tree"]["items"]:
        if item["name"] == source_type:
            recipe_finder = requests.get(f'{sources_url}/{item["name"]}')
            for finder in recipe_finder.json()["payload"]["tree"]["items"]:
                if finder["name"][-4:] == ".yml":
                    recipe_url = f'{sources_url}/{item["name"]}/{finder["name"]}'
                    print("Recipe URL:")
                    print(recipe_url)
                    print("getting example config")
                    yaml = requests.get(recipe_url)
                    for line in yaml.json()["payload"]["blob"]["rawLines"]:
                        yaml_file = f"{yaml_file}\n{line}"
    print(yaml_file)
    return (yaml_file) 

yaml_example = get_example_source()
print_result(query_openai(get_query(), yaml_example))
