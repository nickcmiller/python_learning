import boto3
aws_resource=boto3.resource("s3")
print(aws_resource.buckets.all())