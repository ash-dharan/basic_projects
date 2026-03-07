# main.py CLI

import json

from classes import TodoList
from pathlib import Path

def save_list(file_name,instance):

    file_path = Path(f"./To-do list/{file_name}.json")

    with file_path.open("w") as f:
        json.dump(instance.tasks_list,f)


def load_file(file_name):
    file_path = Path(f"./To-do list/{file_name}.json")

    with file_path.open("r") as f:
        try:
            temp = json.load(f)
        except:
            temp =[]
    
    return temp

while True:

    state = input("Do you want use an existing list or create a new list?(enter new/exist):").lower()
    instance = TodoList()

    if state == "new":
        file_name = input("Enter the name for the list: ").lower()
        Path("./To-do list").mkdir(exist_ok=True)
        Path(f"./To-do list/{file_name}.json").touch()
        break

    elif state == "exist":
        Path("./To-do list").mkdir(exist_ok=True)
        files = [f.stem for f in Path("./To-do list").iterdir()]
        print(files)
        file_name = input("Choose which list to load: ").lower()
        
        if file_name in files:
            instance.load_list(load_file(file_name))
            break
        else:
            print(f"there is no list with name {file_name}")

        
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
        try:
            instance.task_done(task_index)
        except IndexError:
            print("Invalid Index")

    elif option == "3":
        remove_index = int(input("Enter the index of the task you to remove: "))
        try:
            instance.remove_task(remove_index)
        except IndexError:
            print("Invalid Index")

    elif option == "4":
        print(instance)

    elif option == "5":
        save_list(file_name,instance)
    
    elif option == "6":
        print("Goodbye, Thank you for using the program.")
        break