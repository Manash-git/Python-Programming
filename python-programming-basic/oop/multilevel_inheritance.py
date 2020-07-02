class A:
    
    def __init__(self):
        print("Const - A")
    
    def displayA(self):
        print("A")
        
class B(A):
    
    def __init__(self):
        print("Const - B")
    
    def displayB(self):
        print("B")

class C(B):
    
    def __init__(self):
        print("Const - C")
    
    def displayC(self):
        print("C")
    
c= C()
c.displayA()
c.displayB()
c.displayC()


