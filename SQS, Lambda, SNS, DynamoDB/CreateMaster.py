import json

from CreateSNSTopic import create_SNS_topic, create_SNS_subscription

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    state = json.load(file)

###SNS###
#Create topic
state['topic_arn'] = create_SNS_topic(state['topic_name'])

#Create Subscription
state['subscription_response'] = create_SNS_subscription(state['email'], state['topic_arn'], state['topic_name'])

with open("current_state.json", "w") as file:
    # Write the updated data to the file
    json.dump(state, file)

