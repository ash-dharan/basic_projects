# main.py CLI

import json

from classes import TodoList
from pathlib import Path

def save_list(file_name,instance):

    file_path = Path(f"./lists/{file_name}.json")

    with file_path.open() as f:
        json.dump(instance,f)


def load_file(file_name):
    file_path = Path(f"./lists/{file_name}.json")

    with file_path.open() as f:
        temp = json.load(f)
    
    return temp

while True:

    state = input("Do you want use an existing list or create a new list?(enter new/exist):").lower()

    if state == "new":
        file_name = input("Enter the name for the list: ")
        Path.touch(f"./lists/{file_name}.json")
        break

    elif state == "exist":
        print(Path.iterdir("./lists"))
        file_name = input("Choose which list to load: ")

        if file_name in Path.iterdir("./lists"):
            break
        else:
            print(f"there is no list with name {file_name}")


instance = TodoList()
instance.load_list(load_file(file_name))
        

while True:
    print()
    print("========options========")
    print("1 to add new task")
    print("2 to change the status of task")
    print("3 to remove a task")
    print("4 to view the list")
    print("5 to save changes")
    print("6 to exit")
    print()

    option = input("Enter an option: ")
    
    if option == "1":
        new_task = input("Enter the task: ").lower()
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
        save_list(file_name,instance)
    
    elif option == "6":
        print("Goodbye, Thank you for using the program.")
        break