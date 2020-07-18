class Car:
    def __init__(self):
        self.__updateSoftware()
    def display(self):
        print("Update Available.")
    
    # This private method can't be called outside of the class
    
    def __updateSoftware(self):
        print("Updating")

# raptor= Car()
# raptor.display()
# raptor.__updateSoftware()  # This will show an error

class Bike:
    __cc=0
    __brand=""
    
    def __init__(self):
        self.__cc=150
        self.__brand="Yamaha"
    
    def display(self):
        print(self.__cc, self.__brand)
    
    def setCC(self,cc):
        self.__cc=cc

myBike= Bike()
myBike.display()
myBike.setCC(250)
myBike.display()
myBike.__cc=500
myBike.display()      # here you can't access the private var outside the class directly


        