class Student:
    """ Version-1 """
    
    def __init__(self):
        self.name="Manash"
        self.roll=101
    
    def __str__(self):
        return "This is student class."

s=Student()
print(s.name)
print(s.__doc__)
print(s.__str__())
print(s)
print(type(s))