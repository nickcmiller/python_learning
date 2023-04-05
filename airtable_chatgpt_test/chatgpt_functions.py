import os
import openai
import time
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set OpenAI API key using environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def question_chatGPT(question):
    # Wrap API call in a loop and try block that will try 3 times with a 10 sec delay between each try
    for i in range(3):
        try:
            # Generate chat response using OpenAI API
            completion = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[
                {"role": "user", "content": "I am a student preparing to take a technical exam. I want detailed responses to the following practice question or topic. Return the answers in Markdown."},
                {"role": "assistant", "content": "Happy to help! Provide me with the questions or topics and I'll provide a detailed answers for you."},
                {"role": "user", "content": question }
              ]
            )
            
            # Returning the answer from the content of the ChatGPT response
            answer = completion['choices'][0]['message']['content']
            return answer
        except openai.error.APIConnectionError:
            print("try ", i)
            if i == 2:
                raise
            time.sleep(10)  # wait for 10 seconds before retrying