import boto3

#Delete Lambda by the name of the function
def delete_lambda(function_name):
    lambda_client = boto3.client('lambda')
    try:
        response = lambda_client.delete_function(FunctionName=function_name)
        print(f"Deleting Lambda {function_name}", response['ResponseMetadata']['HTTPStatusCode'])
    except Exception as e:
        print(f'Error deleting Lambda function: {e}')