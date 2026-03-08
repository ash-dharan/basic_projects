"TO-DO List app"

class TodoList():

    def __init__(self):
        self.tasks_list = []
    
    def add_task(self,task):
        self.tasks_list.append({
            "task": task,
            "status": False,
            })

    def task_done(self,index):
        (self.tasks_list[index])["status"] = True

    def remove_task(self,index):
        self.tasks_list.pop(index)
    
    def load_list(self,file_list):
        self.tasks_list.extend(file_list)
    
    def __str__(self):
        result = "=======task-list=======\n\n"
        for i in range(len(self.tasks_list)):
            task = self.tasks_list[i]
            if task["status"] :
                result += f" {i} ["+("\u2713")+"]" + f" {task["task"]}" + "\n"
            else:
                result += f" {i} [ ]" + f" {task["task"]}"+'\n'

        return f"{result}"
