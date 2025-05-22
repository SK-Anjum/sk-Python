#Property Decorators: @property, @setter, and @deleter
# Assignment:18
# Create a class Product with a private attribute _price.
# Use @property to get the price, @price.setter to update it,
# and @price.deleter to delete it.

class Product:
    def __init__(self, name, price):
        self.name = name      # Public attribute
        self._price = price   # Private attribute

    @property
    def price(self):
        # Return None or a message if _price is deleted
        return getattr(self, '_price', None)

    @price.setter
    def price(self, value):
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting the price")
        del self._price

p = Product("Bottle", 1000)
print(p.name)    
print(p.price)   

# updating the price
p.price = 800
print(p.price)   

# Deleting the price
del p.price
print(p.price)   