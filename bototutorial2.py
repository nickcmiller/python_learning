import boto3
aws_resource=boto3.resource("s3")
print(resource.buckets.all())