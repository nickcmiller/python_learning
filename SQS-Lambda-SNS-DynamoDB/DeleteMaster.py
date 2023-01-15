import json

from DeleteSNSTopic import delete_SNS_subscription, delete_SNS_topic
from DeleteIAMRole import detach_policies, delete_role, delete_policy
from DeleteSQSQueue import delete_SQS_queue
from DeleteLambda import delete_lambda

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    s = json.load(file)


if "sqs_queue_url" in s:
    if s.get("sqs_queue_url") is not None:
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

running_lambdas = s['running_lambdas']
if len(running_lambdas) > 0:
    keys_to_delete = list(running_lambdas.keys())
    for l in keys_to_delete:
        delete_lambda(l)
        del running_lambdas[l]
        print(running_lambdas)
else:
    print("No Lambdas to Delete")
s['running_lambdas'] = running_lambdas


print(json.dumps(s, indent=2))
# Open the state file for writing
with open("current_state.json", "w") as file:
    # Write the updated state to the file
    json.dump(s, file)
