import boto3
s3_resource=boto3.client("s3")
s3_resource.upload_file(
    Filename="testfile.txt",
    Bucket="totaltechnolog345435341",
    Key="testfile.txt"
)