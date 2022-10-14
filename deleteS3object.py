import boto3
import os
import glob

s3_resource=boto3.client("s3")
#s3_resource.delete_object(Bucket="totaltechnolog345435341", Key="testfile3.txt")

objects = s3_resource.list_objects(Bucket="totaltechnolog345435341")["Contents"]

for object in objects:
    print(object["Key"])

