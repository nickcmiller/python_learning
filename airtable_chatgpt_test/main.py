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
    print(question, " for ", record_id)
    print('\n ------- \n')
    
    answer = question_chatGPT(question)
    print(answer)
    
    write_record(record_id, 
        {
            'ChatGPT Answer': answer
        }
    )       