class Test:
    
    def assign(self):
        self.age=15
    
    def setName(self,n):
        self.__name=n       # Private Variable
    
    def  getName(self):
        return self.__name

    def display(self):
        print("Name: ",self.getName())
        # print("Name: ",self.__name)
        print("Age: ",self.age)
        
        

x= Test()
x.assign()
x.setName("xyz")
x.display()
x.age= 25
x.display()

print()

x.__name="abc"      # Private var value can't be assign this way.
x.display()

              
        
 
    