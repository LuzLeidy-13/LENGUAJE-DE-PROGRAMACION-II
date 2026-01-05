import math
class FiguraGeometica:
    
    def __init__(self,nombre):
        self.nombre = nombre

    def area(self):
        raise NotImplementedError("subclases deben implementar este metodo")
    
    def perimetro(self):
        raise NotImplementedError("subclases deben implementar este metodo")

class Circulo(FiguraGeometica):# esto hace la herencia
    def __init__(self,radio):
        super().__init__("Circulo")
        self.radio = radio

    def area(self):
        return 3.141592* (self.radio**2)

    def perimetro(self):
        return 2*3.141592*self.radio

class Rectangulo(FiguraGeometica):
    def __init__(self, base, altura):
        super().__init__("Rectangulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

circulo = Circulo(5)
print(f"Nombre: {circulo.nombre}")
print(f"Area: {circulo.area ()}")
print(f"Perimetro: {circulo.perimetro()}")

rectangulo = Rectangulo(10, 4)
print(f"Nombre: {rectangulo.nombre}")
print(f"Area: {rectangulo.area()}")
print(f"Perimetro: {rectangulo.perimetro()}")

    
