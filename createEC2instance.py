import boto3 
ec2_resource = boto3.create("ec2")
ec2_resource.create_instances(
    ImageId="ami-05fa00d4c63e32376",
    InstanceType="t1.micro",
    MaxCount=1,
    MinCount=1,
    TagSpecifications=[{'Environment':'Dev'})]
)