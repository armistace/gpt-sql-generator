import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

with open ('intalgo/models/sources.yml', 'r') as source_file:
    sources = source_file.read() 

sources_prompt = f"Using the input dbt sources yaml of {sources} Generate a DBT compliant sql file that answers the question "

query = input("ENTER CHATGPT QUERY: ")

#print(f"{sources_prompt}{query}")

response = openai.Completion.create(model="text-davinci-003", prompt=f"{sources_prompt}{query}", max_tokens=100)
print("############RESPONSE##################")

for line in response.choices:
    print(line.text)
