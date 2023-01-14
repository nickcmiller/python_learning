import boto3
import json

role_name = "Test-Role"
policy_name = "test-policy-role"
description = "A test role"

# Create an IAM client
iam = boto3.client('iam')

# Create the policy document
policy_document = """
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        }
    ]
}
"""

# Create the policy
def create_policy_document(policy):
    policy_response = iam.create_policy(
        PolicyName = policy_name,
        PolicyDocument = json.dumps(policy_document)
    )
    return policy_response['Policy']['Arn']

policy_arn = create_policy_document(policy_document)

assume_role_document = { 
    "Version": "2012-10-17", 
    "Statement": [ 
        {   
            "Effect": "Allow", 
            "Principal": { 
                "Service": "lambda.amazonaws.com" 
            }, 
            "Action": "sts:AssumeRole"
        } 
    ] 
    
}

# Create the role
try:
    create_response = iam.create_role(
        RoleName = role_name,
        AssumeRolePolicyDocument = json.dumps(assume_role_document),
        Description = description
    )
    role_arn = create_response['Role']['Arn']
    print("Role ARN:", role_arn)
    
except Exception as e:
    print("An role creation error occurred: ", e)
try:    
    # Attach the policy to the role
    attach_response = iam.attach_role_policy(
        RoleName = role_name,
        PolicyArn = policy_arn
    )
    print("Policy attached successfully to the role")
except Exception as e:
    print("An error occurred while attaching the policy to the role: ", e)
