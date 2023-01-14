import json

from DeleteSNSTopic import delete_SNS_subscription, delete_SNS_topic
from DeleteIAMRole import detach_policies, delete_role, delete_policy
from DeleteSQSQueue import delete_SQS_queue

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    s = json.load(file)

if "sqs_queue_url" in s:
    delete_SQS_queue(s['sqs_queue_url'], s['sqs_queue_name'])
    del s['sqs_queue_url']
else:
    print("No SQS queue to delete")

if "iam_role_arn" in s:
    detach_policies(s['iam_role_name'])
    delete_role(s['iam_role_name'])
    del s['iam_role_arn']
else:
    print("No IAM role to delete")
    
    
if "iam_policy_arn" in s:
    delete_policy(s['iam_policy_arn'], s['iam_policy_name'])
    del s['iam_policy_arn']
else:
    print("No IAM policy to delete")
    
    
if "topic_arn" in s:
    delete_SNS_topic(s['topic_arn'])
    del s['topic_arn']
    del s['subscription_response']
else:
    print("No Topic to delete")



# Open the state file for writing
with open("current_state.json", "w") as file:
    # Write the updated state to the file
    json.dump(s, file)
