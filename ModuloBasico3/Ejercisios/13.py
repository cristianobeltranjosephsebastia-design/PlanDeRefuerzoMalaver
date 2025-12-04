class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def a_kelvin(self):
        return self.celsius + 273.15

    def __str__(self):
        return f"{self.celsius}°C | {self.a_fahrenheit():.2f}°F | {self.a_kelvin():.2f}K"

temp = Temperatura(30)
print(temp)