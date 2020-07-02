class A:
    
    def display(self):
        print("A")
class B:
    
    def display(self):
        print("B")

class C(A,B):
    pass
    # def display(self):
    #     print("C")
    

x= C()
x.display()

print(C.mro())