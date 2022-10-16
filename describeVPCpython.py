import boto3 
client=boto3.client("ec2")

client.describe_vpcs()