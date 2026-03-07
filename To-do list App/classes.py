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
    
    def __repr__(self):
        for i in range(len(self.tasks_list)):
            result = "======task-list=======\n"
            for task in self.tasks_list:
                if task["status"] :
                    result += f"["+("\u2713")+"]" + f"{task[task]})" + "\n"
                else:
                    result += f"["+("\u2713")+"]" + f"{task[task]}"+'\n'
            return result
