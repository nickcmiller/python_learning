import json

from CreateSNSTopic import create_SNS_topic, create_SNS_subscription
from CreateIAMRole import create_policy_document, create_iam_role, attach_role_policy
from CreateSQSQueue import create_sqs_queue
from CreateLambda import create_lambda

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    s = json.load(file)
    
###IAM###
if "iam_policy_arn" in s:
    print("IAM Policy already created")
else:
    s['iam_policy_arn'] = create_policy_document(s['iam_policy_name'], s['iam_policy_document'])
if "iam_role_arn" in s:
    print("IAM Role already created")
else:
    s['iam_role_arn'] = create_iam_role(s['iam_role_name'], s['iam_assume_role_document'], s['iam_role_description'])
    attach_role_policy(s['iam_role_name'], s['iam_policy_arn'])

##SQS###
if "sqs_queue_url" in s:
    print("SQS queue already created")
else:
     sqs_response = create_sqs_queue(s['sqs_queue_name'])
     if sqs_response is not None:
         s['sqs_queue_url'] = sqs_response

###SNS###
#Create topic
if "topic_arn" in s:
    print("SNS topic already created")
else:
    s['topic_arn'] = create_SNS_topic(s['topic_name'])
    
#Create Subscription
if "subscription_response" in s:
    print("Subscription response already exists")
else:
    s['subscription_response'] = create_SNS_subscription(s['email'], s['topic_arn'], s['topic_name'])


##LAMBDA###
running_lambdas = s['running_lambdas']
for l in s['lambdas']:
    if l in s['running_lambdas']:
        print(l, "is already running")
    else:
        create_lambda(s['iam_role_arn'], s['lambdas'][l])
        running_lambdas[l] = s['lambdas'][l]
s['running_lambdas'] = running_lambdas



print(json.dumps(s, indent=2))
with open("current_state.json", "w") as file:
    # Write the updated data to the file
    json.dump(s, file)



