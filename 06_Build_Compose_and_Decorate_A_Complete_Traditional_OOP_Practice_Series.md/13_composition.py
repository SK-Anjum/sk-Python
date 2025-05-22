#Composition
#Assignment:13
#Create a class Engine and a class Car.
# Use composition by passing an Engine object to the Car class during initialization. 
# Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        print("Engine is starting")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car has an Engine

    def drive(self):
        self.engine.start()
        print("Car is driving")

# Create an instance of Car
obj_car = Car()
obj_car.drive()  # This will start the engine and drive the car


    



            