import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

query = input("ENTER CHATGPT QUERY: ")

response = openai.Completion.create(model="text-davinci-003", prompt=query )
print("############RESPONSE##################")
print(response.choices[0].text)
