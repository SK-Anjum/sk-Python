#Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:15
# Create four classes:
# A with a method show(),
# B and C that inherit from A and override show(),
# D that inherits from both B and C.
# Create an object of D and call show() to observe MRO.

class A:
    def show(self):
        return "Hello from A"
class B(A):
    def show(self):
        return "Hello from B"
class C(A):
    def show(self):
        return "Hello from C"
class D(B,C):           #Diamond Inheritance
    pass
#  Instance of D

d=D()
print(D.mro())      #to check mro of class D

print(d.show())





