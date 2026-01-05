# Principio O (Open/Closed)

class FiguraGeometrica:
    def calcular_area(self):
        raise NotImplementedError("Debe implementar el método calcular_area")
    
    def calcular_perimetro(self):
        raise NotImplementedError("Debe implementar el método calcular_perimetro")

# Principio O y L (Open/Closed y Liskov Substitution)

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        import math
        area = math.pi * (self.radio ** 2)
        return area
    
    def calcular_perimetro(self):
        import math
        perimetro = 2 * math.pi * self.radio
        return perimetro

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        area = self.base * self.altura
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * (self.base + self.altura)
        return perimetro

# Principio D (Dependency Inversion)

class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        area = self.calculadora.calcular_area()
        perimetro = self.calculadora.calcular_perimetro()
        tipo = self.calculadora.__class__.__name__
        print(f"=== {tipo.upper()} ===")
        print(f"Área: {area:.2f}")
        print(f"Perímetro: {perimetro:.2f}")

# Ejecución con Círculo
circulo = Circulo(5)
app = Aplicacion(circulo)
app.ejecutar()

print()

# Ejecución con Rectángulo
rectangulo = Rectangulo(4, 6)
app2 = Aplicacion(rectangulo)
app2.ejecutar()

print()
