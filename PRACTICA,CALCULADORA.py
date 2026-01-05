# Principio O 

class Calculadora:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")

# Principio O y L 
class Suma(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a + self.b

class Resta(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a - self.b

class Multiplicacion(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        return self.a * self.b

class Division(Calculadora):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calcular(self):
        if self.b == 0:
            return "Error: No se puede dividir por cero"
        return self.a / self.b

# Principio D 

class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"El resultado es: {resultado}")

suma = Suma(10, 5)
app = Aplicacion(suma)
app.ejecutar()

resta = Resta(20, 8)
app = Aplicacion(resta)
app.ejecutar()

multiplicacion = Multiplicacion(7, 6)
app = Aplicacion(multiplicacion)
app.ejecutar()

division = Division(50, 10)
app = Aplicacion(division)
app.ejecutar()

division_error = Division(10, 0)
app = Aplicacion(division_error)
app.ejecutar()
