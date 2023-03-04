#!/usr/bin/python
services_list=[];
continue_loop = True;
while continue_loop:
    next_step = input("Add, Remove, or Exit? ")
    print(next_step)
    if next_step == "Add" or next_step =="add":
        new_element= input("Add Service to List: ")
        services_list.append(new_element)
        print("Current List :", services_list)
    elif next_step == "Remove" or next_step =="remove":
        print("Current List :", services_list)
        remove_element= input("What element to remove? ")
        if remove_element in services_list:
            services_list.remove(remove_element)
            print("Current List :", services_list)
        else:
            print("Element not in list. Try again.")
    elif next_step == "Exit" or next_step =="exit":
        print("Now exiting...")
        continue_loop=False
    else:
        print("Not an option. Try again.")