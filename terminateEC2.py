import boto3 
import logging
logging.basicConfig(filename='myapp.log', level=logging.INFO)

ec2_client=boto3.client("ec2", region_name='us-east-1')
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]

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
            logging.info(f"Terminate {instance_id}", )
            terminate_list.append(instance_id)
        else:
            print(i['State']['Name']=='running')
            logging.info(f"Not Dev and not terminating {instance_id}")
logging.info(f"Terminate List: {terminate_list}")
result=ec2_client.terminate_instances(InstanceIds=terminate_list)