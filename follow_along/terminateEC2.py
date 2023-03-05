import logging
import boto3 


#Make logging executable in Lambda and locally
if len(logging.getLogger().handlers) > 0:
    # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
    # `.basicConfig` does not execute. Thus we set the level directly.
    # Reference: https://stackoverflow.com/questions/37703609/using-python-logging-with-aws-lambda
    logging.getLogger().setLevel(logging.INFO)
else:
    logging.basicConfig(level=logging.INFO)

#Set the boto3 client
ec2_client=boto3.client("ec2", region_name='us-east-1')

list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]
terminate_list=[]

for r in reservations:
    instances=r["Instances"]
    for i in instances:
        instance_id = i['InstanceId']
        if i['State']['Name']=='running':
            tags=i['Tags']
            to_terminate=False
            for t in tags:
                if t['Key']=='Environment' and t['Value']=='Dev':
                    to_terminate=True
            if to_terminate:
                logging.info(f"{instance_id} is being terminated", )
                terminate_list.append(instance_id)
            else:
                logging.info(f"{instance_id} is not tagged as Environment:Dev and will not be terminated")
        else:
            logging.info(f"{instance_id} is not running and will not be terminated")
logging.info(f"Terminate List: {terminate_list}")
if(len(terminate_list)>0):
    result=ec2_client.terminate_instances(InstanceIds=terminate_list)
    logging.info(f"Result: {result}")
else:
    logging.info("Terminate List is empty. Nothing to Terminate")