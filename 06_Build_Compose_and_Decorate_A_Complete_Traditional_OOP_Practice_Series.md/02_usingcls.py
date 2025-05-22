#2. Using cls
#Create a class Counter that keeps track of how many objects have been created.
#Use a class variable and a class method with cls to manage and display the count.

class Counter:
    count=0     #class variable

    def __init__(self):
        Counter.count += 1      # increment the count 
        
    @classmethod
    def display_count(cls):
        print(f"Total objects created: {cls.count}")  # display the count using class variable

# objects 
counter1 = Counter()  
counter2 = Counter()  
counter3 = Counter()  
counter4 = Counter()
Counter.display_count()  


