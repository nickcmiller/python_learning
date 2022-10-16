from unittest import result
import boto3 

ec2_client=boto3.client("ec2")
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]
print(len(reservations))

terminate_list=[]
for r in reservations:
    instance_id=r["Instances"][0]['InstanceId']
    tags=r["Instances"][0]['Tags']
    to_terminate=False
    for t in tags:
        if t['Key']=='Environment' and t['Value']=='Dev':
            to_terminate=True
    if to_terminate:
        print("Terminate", instance_id)
        terminate_list.append(instance_id)
    else:
        pass
print("Terminate List: ", terminate_list)
result=ec2_client.terminate_instances(terminate_list)
print(result)