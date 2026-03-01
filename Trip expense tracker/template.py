class Member():
    id = 1
    balance = 0

    def __init__(self,name):
        self.name = name
        self.spentlist = []
        self.id = Member.id
        Member.id += 1
    

    def __str__(self):
        return self.name,self.id,self.balance

class Expenses():

    def __init__(self ,amount ,name ,split=None):
        self.name = name
        self.value = amount
        self.split = split
    
    def set_total(self ,value):
        self.total = value
    
    def __str__(self):
        return f"{(self.name,self.value)}"
    
