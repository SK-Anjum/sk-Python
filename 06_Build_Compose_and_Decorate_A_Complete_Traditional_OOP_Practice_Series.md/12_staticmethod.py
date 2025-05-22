#Static Methods
#Assignment:12
#Create a class TemperatureConverter with a static method 
# celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
#Example usage

celsius = 30
fahrenheit = TemperatureConverter.celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")