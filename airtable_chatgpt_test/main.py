from chatgpt_functions import *
from airtable_functions import *

params = {
    'filterByFormula': 'OR({ChatGPT Answer} = "", NOT({ChatGPT Answer}))'
}
records = get_records(params)

for record in records:
    
    record_id = record['id']
    question = record['fields']['Question']
    
    print('\n ------- \n')
    print("Ask", question, "for Record ID", record_id)
    
    
    answer = question_chatGPT(question)
    print("ChatGPT Answer: ", answer)
    
    response = write_record(record_id, 
        {
            'ChatGPT Answer': answer
        }
    )
    
    print("Airtable Response: ", response)
    print('\n ------- \n')