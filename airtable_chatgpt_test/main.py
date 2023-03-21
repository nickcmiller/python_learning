from chatgpt_functions import *
from airtable_functions import *

# Set up query parameter dictionary for Airtable API that checks for records without filled 'ChatGPT Answer' fields
params = {
    'filterByFormula': 'OR({ChatGPT Answer} = "", NOT({ChatGPT Answer}))'
}

# Get records from Airtable that match the query parameters
records = get_records(params)

# Loop over the records and generate a ChatGPT response for each record with an empty field
for record in records:
    
    # Extract the record ID and question text from the current record
    record_id = record['id']
    question = record['fields']['Question']
    
    print('\n ------- \n')
    print("Ask", question, "for Record ID", record_id)
    
    # Generate a ChatGPT response to the current question
    answer = question_chatGPT(question)
    print("ChatGPT Answer: ", answer)
    
    # Write the ChatGPT response back to the Airtable record
    response = write_record(record_id, 
        {
            'ChatGPT Answer': answer
        }
    )
    
    print("Airtable Response: ", response)
    print('\n ------- \n')