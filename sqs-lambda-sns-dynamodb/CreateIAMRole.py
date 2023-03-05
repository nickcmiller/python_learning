import boto3
import json

# Create an IAM client
iam = boto3.client('iam')

# Create the policy
def create_policy_document(policy_name, policy_document):
    try:
        response = iam.create_policy(
            PolicyName = policy_name,
            PolicyDocument = json.dumps(policy_document)
        )
        print(f'IAM Policy {policy_name} has been created')
        return response['Policy']['Arn']
    except Exception as e:
        print("A policy creation error occurred: ", e)
    
    
# Create the role
def create_iam_role(name, assume_role_document, description):
    try:
        response = iam.create_role(
            RoleName = name,
            AssumeRolePolicyDocument = json.dumps(assume_role_document),
            Description = description
        )
        print(f'IAM Role {name} has been created')
        return response['Role']['Arn']
    except Exception as e:
        print("A role creation error occurred: ", e)
def attach_role_policy(role_name, policy_arn):
    try:    
        # Attach the policy to the role
        attach_response = iam.attach_role_policy(
            RoleName = role_name,
            PolicyArn = policy_arn
        )
        print("IAM Policy attached successfully to the Role")
    except Exception as e:
        print("An error occurred while attaching the policy to the role: ", e)


# # Create the policy document
# policy_document = {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "logs:CreateLogGroup",
#                 "logs:CreateLogStream",
#                 "logs:PutLogEvents"
#             ],
#             "Resource": "arn:aws:logs:*:*:*"
#         }
#     ]
# }

# assume_role_document = { 
#     "Version": "2012-10-17", 
#     "Statement": [ 
#         {   
#             "Effect": "Allow", 
#             "Principal": { 
#                 "Service": "lambda.amazonaws.com" 
#             }, 
#             "Action": "sts:AssumeRole"
#         } 
#     ] 
    
# }