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
        self.tasks.pop(index)
    
    def load_list(self,file_list):
        self.tasks_list.extend(file_list)
    
    def __str__(self):
        for i in range(self.tasks_list):
            print(i,self.tasks_list[i])       
