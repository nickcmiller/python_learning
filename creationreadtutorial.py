import boto3
s3_resource=boto3.client("s3")
list_buckets=s3_resource.list_buckets()
creation_date = list_buckets["Buckets"][0]["CreationDate"]

result = creation_date.strftime("%d/%m/%y")
print(result)