import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Airtable API key and base ID
api_key = os.getenv('YOUR_API_KEY')
base_id = os.getenv('YOUR_BASE_ID')
table_name = os.getenv('YOUR_TABLE_NAME')

def get_records(view=None):
    #Set endpoint for request
    endpoint = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    
    # Set headers and params for API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Set params if they exist
    params = {'view': view} if view else {}
    
    # Send API request and get response
    response = requests.get(endpoint, headers=headers,params=params)
    
    # Get the JSON data from the response
    data = response.json()
    
    records = data['records']
    return records

#pass a JSON object into new_fields where the keys are the fields and the values are the new content
def write_record(record_id, new_fields):
    # endpoint URL
    endpoint = f'https://api.airtable.com/v0/{base_id}/{table_name}/{record_id}'
    
    # Set headers for API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Set new field values for the record
    # new_fields = {
    #     'ChatGPT Answer': 'New Value 1'
    # }
    
    # Set the request body to the new fields
    data = {
        'fields': new_fields
    }
    
    # Send API request and get response
    response = requests.patch(endpoint, headers=headers, json=data)
    
    # Get the JSON data from the response
    data = response.json()
    
    return data

    
# print(get_records()[1])
# print(write_record('rec2WlBdPAq4M5FxL', {
#     'ChatGPT Answer': 'New Value 2'
# }))
    