# Principio O

class CalculadoraGeometrica:
    def calcular(self):
        raise NotImplementedError("Debe implementar el método calcular")

# Principio O y L

class HipotenusaTriangulo(CalculadoraGeometrica):
    def __init__(self, cateto_a, cateto_b):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular(self):
        hipotenusa = (self.cateto_a ** 2 + self.cateto_b ** 2) ** 0.5
        return hipotenusa

# Principio D 
class Aplicacion:
    def __init__(self, calculadora):
        self.calculadora = calculadora

    def ejecutar(self):
        resultado = self.calculadora.calcular()
        print(f"La hipotenusa es: {resultado:}")

hipotenusa = HipotenusaTriangulo(3, 4)
app = Aplicacion(hipotenusa)
app.ejecutar()

