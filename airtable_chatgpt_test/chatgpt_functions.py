import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key using environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

#question to ask ChatGPT
question = "What does this command do? tail $(fgrep -l login /var/log/*)"

# Generate chat response using OpenAI API
completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "I am a student preparing to take a technical exam. I want detailed responses to the following practice questions and topics. Please return the answers in Markdown."},
    {"role": "assistant", "content": "Great! I'd be happy. Please provide me with the questions or topics and I'll do my best to provide detailed answers for you."},
    {"role": "user", "content": question }
  ]
)

print(completion)
