
# Syntax => repr(obj)

import datetime

today= datetime.datetime.now()

print(today)
print()

print(str(today))
print(repr(today))

print()

var= 'foo'

print(repr(var))
print(eval(repr(var)))

class Person():
    
    name="Adam"
    
    def __repr__(self):
        return repr("Hello - " + self.name)

p=Person()

print(repr(p))