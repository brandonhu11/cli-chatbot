from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client()  

response = client.models.generate_content(
    model="models/gemini-3.8-flash",  
    contents="Tell me a joke",
)

print(response.text)
print("---")
print(response.usage_metadata)