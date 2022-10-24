import boto3 

name="test-topic"
endpoint="name@example.com"

sns_client = boto3.client('sns', verify=False)
topic = sns_client.create_topic(Name=name)
print("Created topic ARN ", topic['TopicArn'])

subscription = sns_client.subscribe(TopicArn=topic['TopicArn'], Protocol="email", Endpoint=endpoint, ReturnSubscriptionArn=True)
print("Subscribed ", endpoint, " to ", topic['topicArn'])


