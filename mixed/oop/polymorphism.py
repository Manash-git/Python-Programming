class Dog:
    def sound(self):
        print("Gheu Gheu")

class Cat:
    def sound(self):
        print("Meow Meow")

tom= Dog()
mini= Cat()

def poly(animalTyle):
    animalTyle.sound()

poly(tom)
poly(mini)
