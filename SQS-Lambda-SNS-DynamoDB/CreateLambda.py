import boto3
import shutil
import os
import json

def create_lambda(role_arn, lambda_attributes):
    
    current_directory = os.getcwd()
    target_dir = lambda_attributes['target_dir']
    
    #Determine where you want your file to be zipped to
    target_dir_path = current_directory + "/" + target_dir
    zip_path = current_directory+ "/" + target_dir + "/lambda_handler"
    
    #Get directory path and name for shutil zip
    parent_target_dir_path = os.path.dirname(target_dir_path)
    target_dir_name = os.path.basename(target_dir_path)
    
    #Zip file to target_dir_path
    shutil.make_archive(zip_path, 'zip', root_dir=parent_target_dir_path, base_dir=target_dir_name)
    
    with open(target_dir + "/lambda_handler.zip", "rb") as f:
        zip_bytes = f.read()
    
    # Create a Lambda client
    
    lambda_client = boto3.client('lambda')
    print("Lambda Role", role_arn)
    try:
        response = lambda_client.create_function(
            FunctionName=lambda_attributes['function_name'],
            Runtime=lambda_attributes['runtime'],
            Role=role_arn,
            Handler="lambda_handler",
            Code={
                'ZipFile': zip_bytes
            },
            Description = lambda_attributes['description'],
            Timeout=lambda_attributes['timeout'],
            MemorySize=lambda_attributes['memory_size']
        )
        
        print("Created Lambda ARN is:", response['FunctionArn'])
    except Exception as e:
        print("An error occurred while creating Lambda: ", e)