import boto3
s3_resource=boto3.client("s3")

objects = s3_resource.list_objects(Bucket="totaltechnolog345435341")["Contents"]
print(objects)