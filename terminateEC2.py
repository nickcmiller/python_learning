import boto3 

ec2_client=boto3.client("ec2")
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]
print(len(reservations))

for r in reservations:
    instanceId=r["Instances"][0]['InstanceId']
    tags=r["Instances"][0]['Tags']
    to_terminate=False
    for t in tags:
        if t['Key']=='Environment' and t['Value']=='Dev':
            print(instanceId, t)
            to_terminate=True
    if to_terminate:
        print("Terminate", instanceId)
    else:
        print("Don't terminate", instanceId, "with ", tags)
    

