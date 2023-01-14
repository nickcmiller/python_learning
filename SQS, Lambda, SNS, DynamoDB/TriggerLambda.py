import json
import requests
import argparse

# Create an argument parser
parser = argparse.ArgumentParser()

# Add the queue_url argument
parser.add_argument('--queue-url', required=True, help='The URL of the queue to send message to')

# Parse the arguments
args = parser.parse_args()

# Get the queue URL
queue_url = args.queue_url

data = {'message': 'Hello From Python', 'queue_url': queue_url}
headers = {'Content-type': 'application/json'}

try:
    response = requests.post(url='https://7pxfro4mtd.execute-api.us-east-1.amazonaws.com/dev', data=json.dumps(data), headers=headers)
    response.raise_for_status()
    print(response.status_code)
    print(response.text)
except requests.exceptions.HTTPError as errh:
    print ("Http Error:",errh)
except requests.exceptions.ConnectionError as errc:
    print ("Error Connecting:",errc)
except requests.exceptions.Timeout as errt:
    print ("Timeout Error:",errt)
except requests.exceptions.RequestException as err:
    print ("Something Else:",err)
