#The super() Function
# Assignment:08
# Create a class Person with a constructor that sets the name.
# Inherit a class Teacher from it, add a subject field, and use super()
# to call the base class constructor.

#Parent class
class Person:
    def __init__(self,name):
        self.name = name
#Child class
#Inheriting from Person
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  #  Calling the constructor of the parent class     
        self.subject= subject
    
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")


teacher = Teacher("Anjum","Computer")
teacher.display()

  




       


    
    

        