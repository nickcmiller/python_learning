import boto3 
client=boto3.client("ec2")

vpcs=client.describe_vpcs()
for v in vpcs["Vpcs"]:
    print(v)
    print("--------")