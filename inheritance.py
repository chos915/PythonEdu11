# -*- coding:utf-8 -*-

class Employee:

    def __init__(self, name, tip = 30000):
        self.name = name 
        self.tip = tip 

    def sum_tip(self, amount):
        self.tip += amount 
        return self.tip 
    
class Manager(Employee):

    def __init__(self, name, tip = 50000, project=None):
        Employee.__init__(self, name, tip)
        self.project = project 

    def display(self):
        print("Manager", self.name)

    def sum_tip(self, amount = 0, bonus = 2):
        if amount > 0:
            Employee.sum_tip(self, amount * bonus)
        else:
            Employee.sum_tip(self, amount)

if __name__ == "__main__":
    mng = Manager("Evan")
    print(mng.name) # Evan
    mng.display() # Manager Evan
    print(mng.tip)
    mng.sum_tip(2000)
    print(mng.tip)