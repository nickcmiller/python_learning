import boto3 

ec2_client=boto3.client("ec2")
list_instances=ec2_client.describe_instances()
reservations=list_instances["Reservations"]
print(len(reservations))

for r in reservations:
    print("*************")
    print(r["Instances"][0])
    for i in r["Instances"]:
        print("--------------")
        print(i[''])
        print("--------------")

