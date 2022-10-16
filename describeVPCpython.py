import boto3 
client=boto3.client("ec2")

print(client.describe_vpcs())