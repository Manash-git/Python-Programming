class Demo:
    
    @staticmethod
    def add(x,y):
        print("Sum => ",x+y)
        
x= Demo()
x.add(5,10)

Demo.add(5,6) # Without decorator it's only acces by this calling

