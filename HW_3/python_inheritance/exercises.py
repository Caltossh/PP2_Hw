#exercise 1
class Student(Person):
  person_n = 3
print(Student)  
#!!! example
    
#exercise 2
class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()



