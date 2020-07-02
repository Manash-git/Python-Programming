class Student:
    
    def __init__(self,name, roll):
        self.name=name
        self.roll=roll
        
    def displayS(self):
        print(self.name,self.roll)
        
class Placement:
    
    def __init__(self,company,stud):
        
        self.company=company
        self.stud=stud
    
    def displayA(self):
        self.stud.displayS()
        print(self.company)


s= Student("manash",103)
# s.displayS()
p= Placement("IBM",s)
p.displayA()
