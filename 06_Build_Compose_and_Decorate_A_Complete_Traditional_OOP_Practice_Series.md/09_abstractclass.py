#Abstract Classes and Methods
#Assignment:09
#Use the abc module to create an abstract class Shape with an abstract method area().
#Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod
#Abstract class
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
#Child class
#Inheriting from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
#Creating an object of Rectangle

rectangle = Rectangle(10, 20)
print(f"Area of the rectangle: {rectangle.area()}")  

