import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Airtable API key and base ID
api_key = os.getenv('YOUR_API_KEY')
base_id = os.getenv('YOUR_BASE_ID')

# Table name and endpoint URL
table_name = os.getenv('YOUR_TABLE_NAME')
endpoint = f'https://api.airtable.com/v0/{base_id}/{table_name}'

# Set headers and params for API request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

params = {
    # 'view': 'YOUR_VIEW_NAME' # Optional: specify a view to filter the records
}

# Send API request and get response
response = requests.get(endpoint, headers=headers,params=params)

# Get the JSON data from the response
data = response.json()

# Print the records
for record in data['records']:
    print ("\n---")
    print(record['fields']['Question'])
    print(record['id'])
    print ("---\n")
    print(record)
    