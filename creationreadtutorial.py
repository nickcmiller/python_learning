import boto3
s3_resource=boto3.client("s3")
list_buckets=s3_resource.list_buckets()


result = list_buckets["Buckets"][0]["Creation Date"]
print(result)