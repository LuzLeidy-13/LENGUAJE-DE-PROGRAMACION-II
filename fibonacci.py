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
        tipo = self.calculadora.__class__.__name__
        print(f"\nResultado de {tipo}: {resultado}")

def menu():
    print("\n" + "=" * 40)
    print("CALCULADORA")
    print("=" * 40)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    print("=" * 40)
    
    opcion = input("Seleccione una operación: ")
    
    if opcion in ["1", "2", "3", "4"]:
        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))
            
            if opcion == "1":
                operacion = Suma(a, b)
            elif opcion == "2":
                operacion = Resta(a, b)
            elif opcion == "3":
                operacion = Multiplicacion(a, b)
            elif opcion == "4":
                operacion = Division(a, b)
            
            app = Aplicacion(operacion)
            app.ejecutar()
            
        except ValueError:
            print("\nError: Debe ingresar números válidos.")
        
        menu()

        
    else:
        print("\nOpción inválida. Intente nuevamente.")
        menu()

