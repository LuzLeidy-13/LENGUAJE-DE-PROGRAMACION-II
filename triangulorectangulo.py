from typing import TypeVar, Generic
import math

T = TypeVar("T", int, float)

class TrianguloRectangulo(Generic[T]):
    def __init__(self, cateto_a: T,cateto_b: T):
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_hipotenusa(self) -> int:
        hipotenusa = cateto_a**2 + cateto_b**2
        if hipotenusa< 0:
            raise ValueError("La hipotenusa no está definido para números negativos")

        resultado = 1
        for i in range(1, n + 1):
            resultado *= i

        return resultado
    
    def area(self):


def main():
    try:
        hipotenusa = int(input("Ingrese un número: "))
        cal = CalculadoraFactorial(n)
        print(f"El factorial de {n} es: {cal.calcular_factorial()}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

    
