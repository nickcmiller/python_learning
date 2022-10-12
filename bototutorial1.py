import boto3
aws_resource=boto3.resource("s3")
bucket=aws_resource.Bucket("totaltechnolog345435341")
response = bucket.create(
    ACL='private'
)

print(response)