import json

from CreateSNSTopic import create_SNS_topic, create_SNS_subscription
from CreateIAMRole import create_policy_document, create_iam_role, attach_role_policy
from CreateSQSQueue import create_sqs_queue

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    s = json.load(file)
    
###IAM###    
s['iam_policy_arn'] = create_policy_document(s['iam_policy_name'], s['iam_policy_document'])
s['iam_role_arn'] = create_iam_role(s['iam_role_name'], s['iam_assume_role_document'], s['iam_role_description'])
attach_role_policy(s['iam_role_name'], s['iam_policy_arn'])

###SQS###
s['sqs_queue_url'] = create_sqs_queue(s['sqs_queue_name'])

###SNS###
#Create topic
s['topic_arn'] = create_SNS_topic(s['topic_name'])

#Create Subscription
s['subscription_response'] = create_SNS_subscription(s['email'], s['topic_arn'], s['topic_name'])

with open("current_state.json", "w") as file:
    # Write the updated data to the file
    json.dump(s, file)

