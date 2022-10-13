import boto3
s3_resource=boto3.client("s3")
print(s3_resource.list_buckets())