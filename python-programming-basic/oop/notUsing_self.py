class Test:
    
    def __init__(myself, name, age):
      myself.name = name
      myself.age = age

    def display(self):
        print(self.name,self.age)
        
    def display_test(myself):
        print(myself.name,myself.age)

x=Test("abc",25)
x.display()

print()
x.display_test()

print(x.__dict__)

print()
x.name="John"
x.age=55
print(x.__dict__)