import boto3

# Create an IAM client
iam = boto3.client('iam')

# Detach policies from the role
def detach_policies(role_name):
    try:
        policies_response = iam.list_attached_role_policies(RoleName=role_name)
        for policy in policies_response["AttachedPolicies"]:
            iam.detach_role_policy(RoleName=role_name, PolicyArn=policy["PolicyArn"])
        print("All policies detached successfully from the role: ", role_name)
    except Exception as e:
        print("An error occurred while detaching policies from the role: ", e)

# Delete the role
def delete_role(role_name):
    try:
        iam.delete_role(RoleName=role_name)
        print(f'Role {role_name} deleted successfully.')
    except Exception as e:
        print("An error occurred while deleting the role: ", e)

#Delete the policy
def delete_policy (policy_arn, policy_name):
    try:
        iam.delete_policy(PolicyArn=policy_arn)
        print(f'{policy_name} deleted successfully.')
    except Exception as e:
        print("An error occurred while getting the policy ARN: ", e)