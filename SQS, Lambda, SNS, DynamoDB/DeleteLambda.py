import boto3

function_name = function_name = 'my_lambda_function'
lambda_client = boto3.client('lambda')

try:
    response = lambda_client.delete_function(FunctionName=function_name)
    print(response)
except Exception as e:
    print(f'Error deleting Lambda function: {e}')