# #!/bin/python3

import random
import string

def name_generator(department, number_instances):
    dep = department.lower()
    num = int(number_instances)
    
    if dep in ['marketing', 'accounting', 'finops']:
        name_list = []
        for n in range(0, num):
            rand_list = random.choices(string.ascii_letters+string.digits, k=10)
            name=dep+"-"+''.join(rand_list)
            name_list.append(name)
        return(name_list)
    else:
        return("Your department should not use this name generator")
    
dep_input = input("What is your department? ")
num_input = input("How many instances do you need named? ")

result = name_generator(dep_input, num_input)
print(result)



