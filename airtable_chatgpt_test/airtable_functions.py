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

def get_records(parameters=None):
    #Set endpoint for request
    endpoint = f'https://api.airtable.com/v0/{base_id}/{table_name}'
    
    # Set headers and params for API request
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # Set params if they exist
    params = parameters if parameters else {}
    
    # Send API request and get response
    response = requests.get(endpoint, headers=headers,params=params)
    
    # Get the JSON data from the response
    data = response.json()
    
    records = data['records']
    return records

def extract_id_and_question (records):
    # Create empty list to hold extracted data
    data = []

    # Iterate through records and extract ID and question fields
    for record in records:
        print("Record: ", record)
        record_id = record['id']
        question = record['fields']['Question']
        data.append({'id': record_id, 'question': question})

    return data

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
#     'ChatGPT Answer': "This command will display the last 10 lines (by default) of any files in the /var/log/ directory tree that contain the string \"login\".\n\nThe command uses two basic tools: fgrep and tail.\n\nfgrep is a command-line utility that searches for a fixed string in a file or files. In this command, fgrep is used with the -l option, which means it will only print the names of any files that contain the string \"login\". \n\nThe output of fgrep -l is then used as the argument to the tail command. The $( ) is used to execute the fgrep command first to get the list of files to be tailed. This list of files is then passed as a parameter to the tail command. \n\ntail is a command-line utility that displays the last ten lines (by default) of a file. In this command, tail is used to display the last ten lines of any files in the /var/log/ directory tree that contain the string \"login\". \n\nSo the command will display the last 10 lines for every file in the /var/log/ directory tree that contains the string \"login\""
# }))

# Set params to filter records where "ChatGPT Answer" field is blank or doesn't exist
params = {
    'filterByFormula': 'OR({ChatGPT Answer} = "", NOT({ChatGPT Answer}))'
}

records = get_records(params)
print(records)
print(extract_id_and_question(records))
    