class College:
    
    def __init__(self):
        print("Outer")
        
    class Student:              # Nested Class
        def __init__(self):
            print("Inner")
            
        def displayS(self):
            print("student")
    
    def displayC(self):
        print("college")
        

c= College()
c.displayC()
s= c.Student()
s.displayS()

print()
x= College().Student()
x.displayS()

