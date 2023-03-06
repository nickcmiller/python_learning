import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Define the table name
table_name = 'pg-table'

# Delete the table
try:
    response = dynamodb.delete_table(TableName=table_name)
    print('Table', table_name, 'deleted successfully')
except dynamodb.exceptions.ResourceNotFoundException:
    print('Table', table_name, 'does not exist')