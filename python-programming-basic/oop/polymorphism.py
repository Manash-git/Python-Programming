class A:
    def display(self):
        print("Value => ",0)
    
class B(A):
    def display(self,n):
        print("Value => ",n)

# x=A()
# x.display()

y=B()
y.display(2)
        