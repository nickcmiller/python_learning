import boto3

aws_resource=boto3.client("ec2")

response = aws_resource.create_vpc(CidrBlock='10.0.0.0/16')
print(response)