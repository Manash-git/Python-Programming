
class Test:
    
    def country(self):
        self.city="NYC"
    
x=Test()

print(x.__dict__)

x.country()
print(x.__dict__)
print(x.city)

x.state= "Toronto"

print(x.__dict__)

del x.city
print(x.__dict__)