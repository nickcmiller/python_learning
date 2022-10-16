from unittest import result
import boto3 

ec2_client=boto3.client("ec2", region_name='us-east-1')
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]
print(len(reservations))

terminate_list=[]
for r in reservations:
    instances=r["Instances"]
    for i in instances:
        instance_id = i['InstanceId']
        tags=i['Tags']
        to_terminate=False
        for t in tags:
            if t['Key']=='Environment' and t['Value']=='Dev':
                to_terminate=True
        if to_terminate:
            print("Terminate", instance_id)
            terminate_list.append(instance_id)
        else:
            print("Not terminating", instance_id)
print("Terminate List: ", terminate_list)
# result=ec2_client.terminate_instances(InstanceIds=terminate_list)
# print(result)