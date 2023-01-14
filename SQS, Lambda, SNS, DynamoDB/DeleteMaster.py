import json

from DeleteSNSTopic import delete_SNS_subscription, delete_SNS_topic

# Open the JSON file containing current state
with open("current_state.json", "r") as file:
    # Parse the JSON file
    state = json.load(file)

if "topic_arn" in state:
    print("Deleting topic ", state['topic_name'])
    delete_SNS_topic(state['topic_arn'])
    del state['topic_arn']
    del state['subscription_response']
else:
    print("No topic to delete")




# Open the state file for writing
with open("current_state.json", "w") as file:
    # Write the updated state to the file
    json.dump(state, file)
