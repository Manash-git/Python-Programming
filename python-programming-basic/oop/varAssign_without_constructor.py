# Way - 1

class Employee:
    
    def display(self):
        print("Name: ",self.name)
        print("Company: ",self.company)
        
s= Employee()
s.name="Sruti"
s.company = "Daraz"
s.display()
# print(s.name)
# Employee

# Way - 2
print()
class Student:
    
    def assign(self,exam,gender):
        self.exam=exam
        self.gender=gender
        
    def displayS(self):
        print("Exam: ",self.exam)
        print("Gender: ",self.gender)
        
m= Student()

m.assign("Keya","Female")
m.displayS()