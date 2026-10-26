#This File implements a task tracker 
# Author: Maurice Kutzner
# Date:21.10.2026

import json as j
import pathlib as pathl



def list_task():
    with open("task_tracker.json", "r") as f:
        data = j.load(f)

        for task in data:
            print(f"\nID : \t\t{task.get('id')}")
            print(f"Task: \t\t{task.get('name')}")

            if(task.get('in_prog') == True):
                print('In progress: \tYes')
            else:
                print("In progress: \tNo")

            if(task.get('done') == True):
                print("Done: \t\tYes")
            else:
                print("Done: \t\tNo")

    return

def list_task_done():
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
    for task in data:
        if(task.get('done') == True):
            print(f"\nID : \t\t{task.get('id')}")
            print(f"Task: \t\t{task.get('name')}")
        
            if(task.get('in_prog') == True):
                print('In progress: \tYes')
            else:
                print("In progress: \tNo")
        
            if(task.get('done') == True):
                print("Done: \t\tYes")
            else:
                print("Done: \t\tNo")
    
    return

def list_task_not_done():
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
    for task in data:
        if(task.get('done') == False):
            print(f"\nID : \t\t{task.get('id')}")
            print(f"Task: \t\t{task.get('name')}")
        
            if(task.get('in_prog') == True):
                print('In progress: \tYes')
            else:
                print("In progress: \tNo")
        
            if(task.get('done') == True):
                print("Done: \t\tYes")
            else:
                print("Done: \t\tNo")
    
    return

def list_task_in_prog():
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
    for task in data:
        if(task.get('in_prog') == True):
            print(f"\nID : \t\t{task.get('id')}")
            print(f"Task: \t\t{task.get('name')}")
        
            if(task.get('in_prog') == True):
                print('In progress: \tYes')
            else:
                print("In progress: \tNo")
        
            if(task.get('done') == True):
                print("Done: \t\tYes")
            else:
                print("Done: \t\tNo")
    
    return

def add_task(task_name):
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
        count = len(data)
        data.append({
            'id': count + 1,
            'name': task_name,
            'in_prog': False,
            'done': False
        })
    with open("task_tracker.json", "w") as f:
        j.dump(data,f, indent=4)

    print("task added\n")
    return

def update_task(str_id, task_name_new):
    check = False

    try:    #test for valid input
        ID = int(str_id)        #cast to int to compare ID's later
    except:
        print("No valid input")
        return
    
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
        for task in data:
            if(task.get('id')==ID):
                task.update({'name': task_name_new})
                check = True
                break

    if(check== False):
        print("Task with this ID does not exist\n")
        return
    with open("task_tracker.json", "w") as f:
        j.dump(data,f, indent=4)
    print("Task updated\n")
    return

def mark_done(str_id):
    #test for valid input
    try:
        ID = int(str_id)        #cast to int to compare ID's later
    except:
        print("No valid input")
        return

    
    check = False
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
        print(f"ID: {ID}")
        for task in data:
            print(f"task.get('id'): {task.get('id')}")

            if(task.get('id') == ID):
                task.update({'done': True})
                check = True
                break

    if(check == False):
        print("Task with this ID does not exist\n")
        return

    
    with open("task_tracker.json", "w") as f:
        j.dump(data,f, indent=4)
    print("Task marked done\n")
    return

def mark_in_progr(str_id):
    check = False
    try:
        ID = int(str_id)        #cast to int to compare ID's later
    except:
        print("No valid input")
        return        
        
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
        for task in data:
            if(task.get('id')==ID):
                task.update({'in_prog': True})
                check = True
                break

    if(check == False):
        print("Task with this ID does not exist\n")
        return

    
    with open("task_tracker.json", "w") as f:
        j.dump(data,f, indent=4)
    print("Task marked done\n")
    return

def del_task(str_id):

# We delete by copying the old data into the new_data array and leaving out the element to be deleted

    check = False

    try:
        ID = int(str_id)        #cast to int to compare ID's later
    except:
        print("No valid input")
        return
    with open("task_tracker.json", "r") as f:
        data = j.load(f)
        new_data = []
        i = 0

        #if the ID is bigger than the amount of elements it cannot be valid (important if a very high input is given)
        if(len(data)<ID):
            print("Task with this ID does not exist\n")
            return
        
        for task in data:
           
            if(check == True or task.get('id')!=ID):        #if it is the element to be deleted we add it to our new list
                new_data.append({
                    'id': i + 1,        # update the index to keep consistency
                    'name': task.get('name'),
                    'in_prog': task.get('in_prog'),
                    'done': task.get('done')
                })
                i += 1
                continue
            elif(task.get('id')==ID):       #do nothing to delete the element
                check = True
            
                
    #check valid input
    if(check == False):
        print("Task with this ID does not exist\n")
        return

    #write to file
    with open("task_tracker.json", "w") as f:
        j.dump(new_data,f, indent=4)
    
    print("Task succesfully deleted\n")
    return

def main():

    #if a file already exists open it
    try:
        with open("task_tracker.json", "r") as f:
            pass

    #create the file if it does not exist yet
    except:
        with open("task_tracker.json", "w") as f:
            j.dump([], f)           # add valid JSON 
            pass

    # print the list at the start of the program
    list_task()

    #quality of live functions for easier use

    switch_print = {
        "a": "Name of the task: ",
        "m": "Enter task ID: ",
        "i": "Enter task ID: ",
        "d": "Enter task ID: "
    }

    switch_func = {
        "a": add_task,
        "m": mark_done,
        "i": mark_in_progr,
        "d": del_task
    }

    #loop that runs the task manager

    while(1):
        print(" ")
        print("add task (a) / list task (done /not done/ in progress) (l/ ld / lnd/ li) / update task (u) / mark task done (m) / mark task in progress (i) / delete task (d) / stop program (e)\n")
        x = input()     #get input from user
        x = x.lower()   

        #exit 
        if(x == "e"):
            break

        #print the list
        if(x == "l"):
            list_task()
            continue

        if(x == 'ld'):
            list_task_done()
            continue

        if(x == 'lnd'):
            list_task_not_done()
            continue

        if(x == 'li'):
            list_task_in_prog()
            continue

        #treat the update_task function seperately because it needs two arguments
        
        if (x == "u"):
            print("Enter ID: ")
            a = input()
            print("\nEnter new name: ")
            b = input();
            update_task(a, b)
            continue
        # if it does not fall into any into any encoded letters it was not valid input
        if(x != "a" and x != "m" and x != "i" and x != "d"):
            print("No valid input\n")
            continue

        #ask for necessary input
        print(switch_print.get(x))
        y = input()

        #call the chosen function with the dictionary
        switch_func.get(x)(y)       



main()