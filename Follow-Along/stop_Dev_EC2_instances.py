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

#Set the boto3 client to modify us-east-1 resources
ec2_client=boto3.client("ec2", region_name='us-east-1')

#capture call the instance reservations in us-east-1
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]

#declare list that will collect ids of instances to stop
stop_list=[]

#iterate through instance reservations
for r in reservations:
    instances=r["Instances"]
    #iterate through instances within the reservation
    for i in instances:
        instance_id = i['InstanceId']
        #determine whether instance is running and has a Environment tagged as Dev
        #add matching instance_ids to stop_list
        if i['State']['Name'] == 'running':
            tags=i['Tags']
            to_stop=False
            for t in tags:
                if t['Key']=='Environment' and t['Value']=='Dev':
                    to_stop=True
            if to_stop:
                logging.info(f"{instance_id} is being stopped", )
                stop_list.append(instance_id)
            else:
                logging.info(f"{instance_id} is not tagged as Environment:Dev and will not be stopped")
        else:
            logging.info(f"{instance_id} is not running and will not be stopped")
logging.info(f"Stop List: {stop_list}")

#stop all instance_ids on the stop_list
if(len(stop_list)>0):
    result=ec2_client.stop_instances(InstanceIds=stop_list)
    logging.info(f"Result: {result}")
else:
    logging.info("Stop List is empty. Nothing to stop")