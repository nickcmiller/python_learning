import boto3 

topic_name="Test topic"
subscribe_email="name@example.com"

sns_client = boto3.client('sns', verify=False)
topic = sns_client.create_topic(Name=topic_name)
subscription = sns_client.subscribe(TopicArn=topic['TopicArn'], Protocol="email", Endpoint=subscribe_email, ReturnSubscriptionArn=True)

print("Created topic ARN", topic['TopicArn'])
