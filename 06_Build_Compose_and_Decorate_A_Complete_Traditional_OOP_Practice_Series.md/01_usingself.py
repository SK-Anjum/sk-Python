class Students:
    def __init__(self, name:str, marks:float):
        self.name = name
        self.marks = marks
        
    def display(self):
        print(f"Name: {self.name}, Age: {self.marks}")

student1 = Students("Ayesah", 85)
student1.display()

student2 = Students("Anum", 90)
student2.display()