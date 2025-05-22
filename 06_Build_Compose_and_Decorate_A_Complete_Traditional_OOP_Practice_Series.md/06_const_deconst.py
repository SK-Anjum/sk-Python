#Constructors and Destructors
#Assignment:06
#Create a class Logger that prints a message when an object is created (constructor)
#  and another message when it is destroyed (destructor).


class Logger:
# Constructor   
    def __init__(self):
        print("Object is created")

    def __del__(self):
        print("Object is destroyed")
        

obj= Logger()
    
        