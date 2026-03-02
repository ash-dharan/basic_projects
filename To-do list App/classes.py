"TO-DO List app"

class To_do_list():

    def __init__(self):

        self.list = {}
    
    def add_task(self,task):

        self.list.append(task)

    def task_done(self,index):

        self.list[index] = ''.join(char +'\u0336' for char in self.list[index])

    def remove_task(self,index):

        self.list.pop(index)
