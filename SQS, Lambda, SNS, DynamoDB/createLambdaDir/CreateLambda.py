import boto3
import shutil
import argparse
import os

function_name = 'my_lambda_function'
runtime = 'python3.8'
timeout = 30
memory_size = 128


# Create an argument parser
parser = argparse.ArgumentParser()

# Add the queue_url argument
parser.add_argument('--role-arn', required=True, help='The ARN of the role to attach')

# Parse the arguments
args = parser.parse_args()

# Get the queue URL
role_arn = args.role_arn

# Create a Lambda client
lambda_client = boto3.client('lambda')

handler_name = "lambda_handler.lambda_handler"

# Create a zip file object
current_directory = os.getcwd()
print(current_directory)
shutil.make_archive("lambda_handler", "zip")
with open("lambda_handler.zip", "rb") as f:
    zip_bytes = f.read()

response = lambda_client.create_function(
    FunctionName=function_name,
    Runtime=runtime,
    Role=role_arn,
    Handler=handler_name,
    Code={
        'ZipFile': zip_bytes
    },
    Description='My Lambda function',
    Timeout=timeout,
    MemorySize=memory_size
)

print(response['FunctionArn'])