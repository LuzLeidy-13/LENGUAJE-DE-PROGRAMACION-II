# Principio O (Open/Closed)

class CalculadoraFactorial:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")

# Principio O y L (Open/Closed y Liskov Substitution)

class FactorialNumero(CalculadoraFactorial):
    def __init__(self, numero):
        self.numero = numero

    def calcular(self):
        resultado = 1
        for i in range(1, self.numero + 1):
            resultado *= i
        return resultado

# Principio D (Dependency Inversion)

class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora  # Corrección: era "Calculadora" (con mayúscula)

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"El factorial es: {resultado}")

# Ejecución
factorial = FactorialNumero(5)
app = Aplicacion(factorial)
app.ejecutar()