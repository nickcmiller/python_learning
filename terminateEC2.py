import boto3 
ec2_client=boto3.client("ec2")
list_instances= ec2_client.describe_instances()

print(len(list_instances["Reservations"]))