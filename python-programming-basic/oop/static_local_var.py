
class Student:
    
    # college= 'MIT'      # Way -1 Static
    
    def __init__(self):
        pass
        college='DIU'   # Show Error it is local var and it's scope is only  within the method
        Student.college= 'CMU'
    
    def display(self):
        college= "Harvard"      # Local var
        print("College: ",Student.college) # Calling Class Var
        print("College: ",college)  # Calling Local Var
    

x= Student()
x.display()

y= Student()
Student.college= "BUET"
y.display()