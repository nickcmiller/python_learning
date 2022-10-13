import boto3
s3_resource=boto3.client("s3")
s3_resource.list_buckets()