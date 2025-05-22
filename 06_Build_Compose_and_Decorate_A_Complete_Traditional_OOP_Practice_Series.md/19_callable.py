#callable() and __call__()
#Assignment:19
#Create a class Multiplier with an __init__() to set a factor.
# Define a __call__() method that multiplies an input by the factor. 
# Test it with callable() and by calling the object like a function.#

class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # Store the factor

    def __call__(self, number):
        # method to make the object to be called like a function
        return number * self.factor

# Create an instance with factor 5
multiplier = Multiplier(7)

# Test callable
print(callable(multiplier))  

# Call the object like a function
result = multiplier(40)  
print(result)