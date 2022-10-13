import boto3
import os
import glob

s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="testfile.txt",
    Bucket="totaltechnolog345435341",
    Key="testfile.txt"
)

n=0
cwd=os.getcwd()
while n < 4:
    print(n, cwd, glob.glob("*.txt"))
    s3_resource.upload_file(
        Filename="testfile.txt",
        Bucket="totaltechnolog345435341",
        Key="testfile"+n+".txt"
    )
    n+=1