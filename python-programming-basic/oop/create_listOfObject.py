class Student:
    
    def __init__(self, name, age):
      self.name = name
      self.age = age
    
    def display(self):
        print("Name: %s\nAge: %i"%(self.name,self.age))
        
# s=Student("abc",50)
# s.display()

s=[Student("abc",25),
   Student("xyz",30),
   Student("pqr",55)]

for i in s:
    i.display()
    print()