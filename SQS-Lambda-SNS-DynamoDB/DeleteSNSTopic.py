import boto3
# Delete the subscription
def delete_SNS_subscription(subscription_arn):
    # Create an SNS client
    sns = boto3.client('sns')
    try:
        # Delete the SNS subscription
        response = sns.unsubscribe(SubscriptionArn=subscription_arn)
        print(f'Subscription with ARN {subscription_arn} is deleted')
    except Exception as e:
        print(f'An error occurred while deleting the subscription {subscription_arn}: {e}')

#Delete SNS topic
def delete_SNS_topic(topic_arn):
    # Create an SNS client
    sns = boto3.client('sns')
    try:
        # Delete the SNS topic
        response = sns.delete_topic(TopicArn=topic_arn)
        print(f'Topic with ARN {topic_arn} is deleted')
    except Exception as e:
        print(f'An error occurred while deleting the topic {topic_arn}: {e}')
