import json
import os
from datetime import datetime
import boto3

QUEUE_NAME = os.environ['QUEUE_NAME']

sqs = boto3.client('sqs')

def lambda_handler(event, context):
    #Capturing time message received by Lambda
    current_time = datetime.now().strftime('%H:%M:%S on %Y-%m-%d')
    
    #Capture the message sent
    queue_message = event['body']
    
    #Create message for response
    response_message = f'Sent message "{queue_message}" to SQS at {current_time}'
    print("Response Message: ", response_message)
    
    #Sending message to SQS Queue
    queue = sqs.get_queue_url(QueueName=QUEUE_NAME)
    queue_url = queue['QueueUrl']
    print("Queue Url: ", queue_url)
    response = sqs.send_message(QueueUrl = queue_url, MessageBody = queue_message)
    
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(response)
    }

