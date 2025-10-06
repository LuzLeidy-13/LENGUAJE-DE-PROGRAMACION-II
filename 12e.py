class Temperatura:
    def __init__(self, celsius):
        self.celsius = celsius
        print(f"Temperatura inicializada en {self.celsius}°C.")

    def a_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def __del__(self):
        print("Objeto Temperatura destruido.")

celsius = float(input("Ingrese la temperatura en °C: "))

temp1 = Temperatura(celsius)
print(f"temperatura en c°: {temp1.celsius}")
print(f"Temperatura en °F: {temp1.a_fahrenheit()}")

del temp1

try:
    temp1.a_fahrenheit()
except NameError:
    print("objeto temperatura dstruido")
