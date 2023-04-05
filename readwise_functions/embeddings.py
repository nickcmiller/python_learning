import os
import requests
import json
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def create_embedding(text):
    text = text.replace("\n", " ")
    response = openai.Embedding.create(
        input=text,
        model="text-embedding-ada-002"
    )
    
    embedding = response['data'][0]['embedding']
    
    return response
    
create_embedding("Test")