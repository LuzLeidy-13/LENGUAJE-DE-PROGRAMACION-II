import math
class Cuadrado:
    def area(self):
        lado = 4
        area = lado ** 2
        print(f"El área del cuadrado es {area}")

class Rectangulo:
    def area(self):
        base = 5
        altura = 3
        area = base * altura
        print(f"El área del rectángulo es {area}")

class Circulo:
    def area(self):
        radio = 2
        area = math.pi * (radio ** 2)
        print(f"El área del círculo es {area}")

def calcularArea(objeto):
    objeto.area()

objetos = [Cuadrado(), Rectangulo(), Circulo()]
for objeto in objetos:
    calcularArea(objeto)
