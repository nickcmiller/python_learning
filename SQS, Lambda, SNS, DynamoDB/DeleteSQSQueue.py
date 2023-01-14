import boto3

sqs = boto3.client('sqs')

# Try to delete the queue and return the result
def delete_SQS_queue(queue_url, queue_name):
    try: 
        result = sqs.delete_queue(QueueUrl=queue_url)
        print(f'SQS Queue {queue_name} deleted')
    except sqs.exceptions.QueueDoesNotExist:
        print('Queue does not exist')
    except sqs.exceptions.ClientError:
        print('Error accessing queue')