import boto3 
ec2_resource = boto3.resource("ec2")
tags=[{'Key':'Environment','Value':'Dev'}]
result = ec2_resource.create_instances(
    ImageId="ami-05fa00d4c63e32376",
    InstanceType="t1.micro",
    MaxCount=3,
    MinCount=2,
    TagSpecifications=[{'ResourceType': 'instance','Tags':tags}]
)
print(result)