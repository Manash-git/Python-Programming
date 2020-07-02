class Student1:
    
    """ Custom Method V-1 """
    
    def __init__(self,name,roll,section):
        self.name=name
        self.roll=roll
        self.section=section
        
    
    def display(self):
        print('Name: ',self.name)
        print('Roll: ',self.roll)
        print('Section: ',self.section)
        
    def __str__(self):
        return "Hello python"

s= Student1("Hello",105,'A')
s.display()

print(s)
print(s.name)
# print(s.__init__())
s.__init__('Priya',255,'B')
s.display()

        
    