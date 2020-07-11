class MyClass:
    def __init__(self, name, age):
      self.name = name
      self.age = age
    def display(self):
        print(self.name,self.age)
    # if we want to avoid self parameter use @staticmethod
    
    @staticmethod
    def test():
        print("hello")

MyClass("Manash",30).display()
cls=MyClass("mondal",50)
cls.test()

