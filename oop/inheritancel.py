# inheritance
class Animal:
    def whoAmI(self):
        print("I am Animal")
        
class Dog(Animal):
    def bark(self):
        print("Barking")
        
    # method overriding
    def whoAmI(self):
        print("I am a dog")

tom= Dog()
tom.bark()
tom.whoAmI()
