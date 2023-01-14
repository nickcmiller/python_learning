import boto3
import shutil
import os

function_name = 'API_to_SQS'
runtime = 'python3.8'
timeout = 30
memory_size = 128


# Create a Lambda client
lambda_client = boto3.client('lambda')

handler_name = "lambda_handler.lambda_handler"

# Create a zip file object
current_directory = os.getcwd()
print(current_directory)
shutil.make_archive("/APItoSNSLambdaDir/lambda_handler", "zip", base_dir="/APItoSNSLambdaDir/")

# with open("lambda_handler.zip", "rb") as f:
#     zip_bytes = f.read()

# response = lambda_client.create_function(
#     FunctionName=function_name,
#     Runtime=runtime,
#     Role=role_arn,
#     Handler=handler_name,
#     Code={
#         'ZipFile': zip_bytes
#     },
#     Description='My Lambda function',
#     Timeout=timeout,
#     MemorySize=memory_size
# )

# print(response['FunctionArn'])