import boto3 

name="test-topic"
endpoint="name@example.com"

sns_client = boto3.client('sns', verify=False)
topic = sns_client.create_topic(Name=name)
topicARN=topic['TopicArn']
print("Created topic ARN ", topicARN)

subscription = sns_client.subscribe(TopicArn=topicARN, Protocol="email", Endpoint=endpoint, ReturnSubscriptionArn=True)
print("Subscribed ", endpoint, " to ", topicARN)


