import os
import dotenv
from openai import AzureOpenAI

dotenv.load_dotenv()

client = AzureOpenAI(
  api_key = os.getenv("AZURE_OPENAI_API_KEY"),  
  api_version = "2024-02-15-preview",
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")  # Your Azure OpenAI resource's endpoint value.
)

conversation=[{"role": "system", 
               "content": [{
				"type": "text",
				"text": "You are chat which is very friendly and funny in nature."
			}]}]

while True:
    user_input = input("Q:")   
    if user_input.lower() in ["exit", "quit"]:
        break   
    conversation.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="Myntabot", 
        messages=conversation
    )

    conversation.append({"role": "assistant", "content": response.choices[0].message.content})
    print("\n" + response.choices[0].message.content + "\n")