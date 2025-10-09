class SumaNaturales:
    def _init_(self, limite):
        self.limite = limite
        self.suma = 0

    def calcularSuma(self):
        for i in range(1, self.limite + 1):
            self.suma += i
            if i % 2 == 0:
                print(f"{i} es par")
            else:
                print(f"{i} es impar")
        return self.suma

def main():
    miSuma = SumaNaturales(10)
    resultado = miSuma.calcularSuma()
    print(f"La suma de los primeros {miSuma.limite} números naturales es: {resultado}")

if _name_ == "_main_":
    main()
