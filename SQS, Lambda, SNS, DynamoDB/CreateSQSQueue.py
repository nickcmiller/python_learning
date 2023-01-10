import boto3

# Create an SQS client
sqs = boto3.client('sqs')

# Create a new SQS queue
response = sqs.create_queue(
    QueueName='my-queue',
    Attributes={
        'DelaySeconds': '60',
        'MessageRetentionPeriod': '86400'
    }
)

# Print the URL of the new queue
print(response['QueueUrl'])