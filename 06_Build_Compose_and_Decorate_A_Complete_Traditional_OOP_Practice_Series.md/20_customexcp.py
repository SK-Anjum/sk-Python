#Creating a Custom Exception
#Assignment:20
#Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18. 
# Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be at least 18 or older."):
        self.age = age
        self.message = f"Invalid age {age}: {message}"
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    else:
        print(f"Age {age} is valid.")

try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(f"Error: {e}")
except ValueError:
    print("Please enter a valid integer for age.")