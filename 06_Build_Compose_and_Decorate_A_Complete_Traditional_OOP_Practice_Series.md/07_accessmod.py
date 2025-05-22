#Access Modifiers: Public, Private, and Protected
#Assignment:07
# Create a class Employee with:
# a public variable name,
# a protected variable _salary, and
# a private variable __ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employ:
    def __init__(self, name, salary, ssn):
        self.name= name
        self._salary= salary
        self.__ssn = ssn

emp =Employ("Anjum",55000, "122-324-154")
print("Public variable:", emp.name)
print("Protected variable:",emp._salary)
try:
    print("Private variable:", emp.__ssn)
except AttributeError:
    print("Can not access private varible")




