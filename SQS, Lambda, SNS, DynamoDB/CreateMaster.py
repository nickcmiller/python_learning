import boto3
from CreateSNSTopic import create_SNS_topic, create_SNS_subscription

#SNS topic name
topic_name = 'test-topic'
# The email address to subscribe to SNS topic
email = 'nick@example.com'

topic_arn = create_SNS_topic(topic_name)
subscription_response = create_SNS_subscription(email, topic_arn, topic_name)
print(topic_arn, subscription_response)



