import boto3

role_name = "Test-Role"
policy_name = "test-policy-role"

import boto3

# Create an IAM client
iam = boto3.client('iam')

# Detach policies from the role
try:
    policies_response = iam.list_attached_role_policies(RoleName=role_name)
    for policy in policies_response["AttachedPolicies"]:
        iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
    print("All policies detached successfully from the role: ", role_name)
except Exception as e:
    print("An error occurred while detaching policies from the role: ", e)

# Delete the role
try:
    iam.delete_role(RoleName=role_name)
    print("Role deleted successfully.")
except Exception as e:
    print("An error occurred while deleting the role: ", e)
    
#List attached policies
try:
    all_policies_response = iam.list_policies()
    policy_arn = None
    for policy in all_policies_response["Policies"]:
        if policy['PolicyName'] == policy_name:
            policy_arn = policy['Arn']
            break
    if policy_arn:
        print(f"{policy_name} arn is :{policy_arn}")
        iam.delete_policy(PolicyArn=policy_arn)
        print(f"{policy_name} deleted successfully.")
        
    else:
        print(f"{policy_name} not found")
except Exception as e:
    print("An error occurred while getting the policy ARN: ", e)