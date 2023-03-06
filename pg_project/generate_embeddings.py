import json
import boto3
import time
import os
from botocore.exceptions import ClientError

# configure OpenAI API
# openai_api_key = os.getenv('OPENAI_API_KEY')
openai_model = "text-embedding-ada-002"
openai_url = "https://api.openai.com/v1/engines/" + openai_model + "/completions"

# configure DynamoDB
dynamodb = boto3.resource("dynamodb")
table_name = "pg-table"
table = dynamodb.Table(table_name)


def generate_embeddings(essays):
    items_to_write = []
    index = 1 
    for i, section in enumerate(essays):
        for j, chunk in enumerate(section["chunks"]):
            print(index)
            if index < 26:
                essay_title = chunk["essay_title"]
                essay_url = chunk["essay_url"]
                essay_date = chunk["essay_date"]
                essay_thanks = chunk["essay_thanks"]
                content = chunk["content"]
                content_length = chunk["content_length"]
                content_tokens = chunk["content_tokens"]
    
                # generate embedding with OpenAI API
                # response = requests.post(
                #     openai_url,
                #     headers={"Content-Type": "application/json", "Authorization": "Bearer " + openai_api_key},
                #     json={"prompt": content, "max_tokens": 128, "model": openai_model}
                # )
                
                # embedding = response.json()["choices"][0]["text"]
                
                embedding = []
                
                # save data to items_to_write list
                item = {
                    "index": index,
                    "essay_title": essay_title,
                    "essay_url": essay_url,
                    "essay_date": essay_date,
                    "essay_thanks": essay_thanks,
                    "content": content,
                    "content_length": content_length,
                    "content_tokens": content_tokens,
                    "embedding": embedding
                }
                items_to_write.append(item)
                
                # write to DynamoDB every 25 items
                if len(items_to_write) == 25 or (i == len(essays) - 1 and j == len(section["chunks"]) - 1):
                    with table.batch_writer() as batch:
                        for item in items_to_write:
                            print(item['index'], item['essay_title'])
                            batch.put_item(Item=item)
                    print(f"Wrote {len(items_to_write)} items to DynamoDB.")
                    items_to_write = []
                    time.sleep(0.2)  # limit API requests to once every 0.2 seconds
            else:
                break
            index += 1

if __name__ == "__main__":
    with open("json_storage/pg_data.json", "r") as file:
        book = json.load(file)

    generate_embeddings(book["essays"])