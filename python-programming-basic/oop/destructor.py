class Test:
    
    def __init__(self):
        print("constructor")
        
    def display(self):
        print("Display Called")
        
    def __del__(self):
        print("Destructor")
        
Test().display()