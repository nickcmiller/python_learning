import boto3
import json
ec2_resource = boto3.resource("ec2", region_name='us-east-1')
tags=[{'Key':'Environment','Value':'Dev'}]

def lambda_handler(event, context):
    result = ec2_resource.create_instances(
        ImageId="ami-05fa00d4c63e32376",
        InstanceType="t1.micro",
        MaxCount=1,
        MinCount=1,
        TagSpecifications=[{'ResourceType': 'instance','Tags':tags}]
    )
    for i in result: 
        print(i.id, " has been launched")
