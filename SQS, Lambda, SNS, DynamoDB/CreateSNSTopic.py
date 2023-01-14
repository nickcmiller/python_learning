import boto3

#function to create an SNS topic
def create_SNS_topic(name):
    #Declaring ARN variable for later use
    topic_arn = '' 
    
    # Create an SNS client
    sns = boto3.client('sns')
    
    try:
        # Create a new SNS topic
        response = sns.create_topic(Name=name)
        # Print the ARN of the new topic
        topic_arn = response['TopicArn']
        print(f'Topic {name} is ARN {topic_arn}')
    except Exception as e:
        print(f'An error occurred while creating the topic {name}: {e}')
    return topic_arn

# Create the subscription
def create_SNS_subscription(email, topic_arn, topic_name):
    sns = boto3.client('sns')
    subscription_arn = ''
    try:
        response = sns.subscribe(
            TopicArn=topic_arn,
            Protocol='email',
            Endpoint=email
        )
        #capture subscription ARN in a variable 
        subscription_arn = response['SubscriptionArn']
        # Print the subscription ARN
        print(f'{email} subscription is {subscription_arn}')
    except Exception as e:
        print(f'An error occurred while subscribing {email} to topic {topic_name}): {e}')
    return response['SubscriptionArn']
