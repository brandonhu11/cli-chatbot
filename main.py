from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()  

while True:
    name = input("What's your name? ")

    if name.lower() == "quit":
        print("Bye!")
        break

    print("Hi " + name + "!")

response = client.models.generate_content(
    model="models/gemini-3.8-flash",  
    contents="Tell me a joke",
)

print("Bot: ", response.text)