
class A:
    
    def display_A(self):
        print("A")


class B(A):
    
    def display_B(self):
        print("B")

class C(A):
    
    def display_C(self):
        print("C")

class D(B,C):
    
    def display_D(self):
        print("D")
x=D()
x.display_A()
x.display_B()
x.display_C()
x.display_D()
