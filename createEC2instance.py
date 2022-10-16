import boto3 
ec2_resource = boto3.resource("ec2")
tags=[{'Key':'Environment','Value':'Dev'}]
result = c2_resource.create_instances(
    ImageId="ami-05fa00d4c63e32376",
    InstanceType="t1.micro",
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[{'ResourceType': 'instance','Tags':tags}]
)
print(result)