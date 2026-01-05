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
    def __init__(self, calculadora, nombre):
        self.calculadora = calculadora
        self.nombre = nombre

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"La {self.nombre} es: {resultado}")


a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

suma = Suma(a, b)
app = Aplicacion(suma, "Suma")
app.ejecutar()

resta = Resta(a, b)
app = Aplicacion(resta, "Resta")
app.ejecutar()

multiplicacion = Multiplicacion(a, b)
app = Aplicacion(multiplicacion, "Multiplicacion")
app.ejecutar()

division = Division(a, b)
app = Aplicacion(division, "Division")
app.ejecutar()
