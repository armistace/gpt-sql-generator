import os
import openai
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = "org-OzlolStjF4eoUeYq6meETBmQ"

def query_openai(query):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[
            {"role": "user", "content": f"{query}"},
            ], max_tokens=1000)
    return response

def get_query():
    query = input("What is your query?: ")
    return query

def print_result(response):
    print(f"Result")
    print(f"{response}")

print_result(query_openai(get_query()))
