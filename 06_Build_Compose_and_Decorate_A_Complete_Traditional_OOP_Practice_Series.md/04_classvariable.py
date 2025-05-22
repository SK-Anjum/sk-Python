#Class Variables and Class Methods
#Assignment:04
# Create a class Bank with a class variable bank_name.
# Add a class method change_bank_name(cls, name) that allows changing the bank name. 
# Show that it affects all instances.

class Bank:
    bank_name="ABC BANK"
    @classmethod

    def change_bank_name(cls, name):
        cls.change_bank_name=name
    
user1=Bank() 
user2=Bank()

print("Before changing Bank Name")
print(f"user1: {user1.bank_name}")
print(f"user2: {user2.bank_name}")

Bank.change_bank_name="XYZ Bank"

print("After changing bank name")

print(f"user1: {user1.change_bank_name}")
print(f"user2: {user2.change_bank_name}")




    




