import requests


sources_url = "https://github.com/datahub-project/datahub/tree/master/metadata-ingestion/docs/sources"

sources = requests.get(sources_url)

print ("Please Select source from list below: ")
for name in sources.json()["payload"]["tree"]["items"]:
    print (name["name"])

source_type = input("Please input source: ")

for item in sources.json()["payload"]["tree"]["items"]:
    if item["name"] == source_type:
        recipe_finder = requests.get(f'{sources_url}/{item["name"]}')
        for finder in recipe_finder.json()["payload"]["tree"]["items"]:
            if finder["name"][-4:] == ".yml":
                recipe_url = f'{sources_url}/{item["name"]}/{finder["name"]}'
                print("Recipe URL:")
                print(recipe_url)
                print("getting recipe")
                yaml = requests.get(recipe_url)
                yaml_file = ""
                for line in yaml.json()["payload"]["blob"]["rawLines"]:
                    yaml_file = f"{yaml_file}\n{line}" 
                print(yaml_file)

