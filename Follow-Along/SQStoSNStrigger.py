import json
import os
import boto3

client = boto3.client('sns')
TOPIC_ARN= os.environ['TOPIC_ARN']

def lambda_handler(event, context):
    
    received_sqs_records = event['Records']
    
    for r in received_sqs_records: 
    
        message = r['body']
        print("Message from SQS: ", message, type(message))
        
        response = client.publish(
            TopicArn=TOPIC_ARN,
            Message=json.dumps({'default': json.dumps(message)}),
            MessageStructure='json'
        )
    
    return {
        'statusCode': 200,
        'body': received_sqs_records
    }

