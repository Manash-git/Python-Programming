
class A:
    
    def display_A(self):
        print("A")
class B:
    
    def display_B(self):
        print("B")

class C(A,B):
    
    def display_C(self):
        print("C")

x= C()
x.display_C()
x.display_A()
x.display_B()