import boto3
aws_resource=boto3.resource("s3")
print(list(aws_resource.buckets.all()))

for bucket in aws_resource.buckets.all():
    print(bucket.name)