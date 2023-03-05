import boto3

# Create an SQS client
sqs = boto3.client('sqs')


def create_sqs_queue(name):
    try:
        # Create a new SQS queue
        response = sqs.create_queue(
            QueueName=name,
            Attributes={
                'DelaySeconds': '60',
                'MessageRetentionPeriod': '86400'
            }
        )
        # Print the URL of the new queue
        print(f'SQS Queue {name} has been created')
        return response['QueueUrl']
    except Exception as e:
        print("An error occurred: ", e)