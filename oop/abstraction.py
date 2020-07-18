from abc import ABC,abstractclassmethod

class Shape(ABC):
    @abstractclassmethod
    def area(self):pass
    
    @abstractclassmethod
    def perimeter(self):pass

class Square(Shape):
    def __init__(self,side):
        self.__side=side
    def area(self):
        print(self.__side*self.__side)
    def perimeter(self):
        print(self.__side*4)

mySqr=Square(5)
mySqr.area()
mySqr.perimeter()

mySqr=Square(8)
mySqr.area()
mySqr.perimeter()