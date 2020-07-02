class Student:
    
    def __init__(self):
        self.name=""
        self.roll=0
    
    def assignS(self,n,r):
        self.name=n
        self.roll=r
    
    def display(self):
        print(self.name,self.roll)

class Placement(Student):
    def __init__(self):
        self.company=""
        self.salary=0
        
    def assignP(self,c,s):
        self.company=c
        self.salary=s
        
    def displayP(self):
        print(self.company,self.salary)
        
p=Placement()
p.assignP("Daraz",25000)
p.displayP()

print()
p.assignS("Priya",105)
p.display()