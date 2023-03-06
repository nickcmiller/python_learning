import boto3

# Create a DynamoDB client
dynamodb = boto3.client('dynamodb')

# Check if the table exists
table_name = 'pg-table'
try:
    response = dynamodb.describe_table(TableName=table_name)
    if response['Table']['TableStatus'] == 'ACTIVE':
        print('Table', table_name, 'already exists')
except dynamodb.exceptions.ResourceNotFoundException:
    # Create the table schema
    table_schema = {
        'AttributeDefinitions': [
            {'AttributeName': 'index', 'AttributeType': 'N'}
        ],
        'KeySchema': [
            {'AttributeName': 'index', 'KeyType': 'HASH'}
        ],
        'BillingMode': 'PAY_PER_REQUEST',
        'TableName': table_name
    }
    
    # Create the table
    response = dynamodb.create_table(**table_schema)

    # Wait for the table to be created
    dynamodb.get_waiter('table_exists').wait(TableName=table_name)

    print('Table', table_name, 'created successfully')