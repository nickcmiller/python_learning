import argparse
import boto3

# Create an argument parser
parser = argparse.ArgumentParser()

# Add the queue_url argument
parser.add_argument('--queue-url', required=True, help='The URL of the queue to delete')

# Parse the arguments
args = parser.parse_args()

# Get the queue URL
queue_url = args.queue_url

# Create an SQS client
sqs = boto3.client('sqs')

# Delete the queue
result = sqs.delete_queue(QueueUrl=queue_url)
print(result)