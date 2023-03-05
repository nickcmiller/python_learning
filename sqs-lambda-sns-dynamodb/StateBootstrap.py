import json
with open("current_state.json", "r") as file:
    # Parse the JSON file
    s = json.load(file)

s['lambdas'] = {}
s['running_lambdas'] = {}

api_sqs_lambda = {}
api_sqs_lambda['function_name'] = 'API_to_SQS'
api_sqs_lambda['runtime'] = 'python3.8'
api_sqs_lambda['timeout'] = 30
api_sqs_lambda['memory_size'] = 128
api_sqs_lambda['description'] = 'My Lambda function'
api_sqs_lambda['target_dir'] = "APItoSQSLambdaDir"

s['lambdas'][api_sqs_lambda['function_name']] = api_sqs_lambda


print(s)
with open("current_state.json", "w") as file:
    # Write the updated data to the file
    json.dump(s, file)

