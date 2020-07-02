class Student:
    """ Contructor with parameter"""
    
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        
    def __str__(self):
        return "Hello Python"
    

# s=Student("manash",105)
s=Student("Mondal","161")
print(s.name)
print(s.roll)
print(s)
print(s.__doc__)


        