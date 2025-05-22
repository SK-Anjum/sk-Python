#Static Variables and Static Method
# Assignment:05
#Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.

class MathUtils: 
    @staticmethod
    def add(a, b):
        return a + b
    
    #  static method
print(MathUtils.add(5, 10))