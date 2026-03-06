# main.py CLI

import json

from classes import TodoList
from pathlib import Path

def save_list(file_name,instance):

    file_path = Path(f"./{file_name}")

    with file_path.open() as f:
        json.dump(instance,f)


def load_file(file_name):
    file_path = Path(f"./{file_name}")

    with file_path.open() as f:
        temp = json.load(f)
    
    return temp

# def intialize_list(file_name):
#     temp = load_file(file_name)
#     result = TodoList()

#     for element in temp:
#         result.add_task(element)
    
#     return result



while True:

    state = input("Do you want use an existing list or create a new list?(enter new/exist):").lower()

    if state == "new":
        break

    elif state == "exist":
        break

instance = TodoList()
instance.load_list(load_file())
        

while True:

    print("========options========")
    print("1 for add new task")
    print("2 for change the status of task")
    print("3 for remove a task")
    print("4 view the list")
    print("5 to save changes")
    print("6 to exit")

    option = input("Enter an option: ")

    
    if option == "1":
        new_task = input("Enter the task:").lower()
        instance.add_task(new_task)

    elif option == "2":
        task_index = int(input("Enter the index of the task: "))
        instance.task_done(task_index)

    elif option == "3":
        remove_index = int(input("Enter the index of the task you to remove: "))
        instance.remove_task(remove_index)

    elif option == "4":
        print(instance)

    elif option == "5":
        save_list()
    
    elif option == "6":
        print("Goodbye, Thank you for using the program.")
        break