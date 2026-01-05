from typing import TypeVar, Generic
import math

T = TypeVar("T", int, float)

class TrianguloRectangulo(Generic[T]):
    def __init__(self, cateto_a: T, cateto_b: T):  # corregido __init__
        self.cateto_a = float(cateto_a)
        self.cateto_b = float(cateto_b)

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.cateto_a**2 + self.cateto_b**2)  # fórmula corregida

    def calcular_area(self) -> float:
        return (self.cateto_a * self.cateto_b) / 2

    def calcular_perimetro(self) -> float:
        return self.cateto_a + self.cateto_b + self.calcular_hipotenusa()


def main():
    try:
        a = float(input("Ingrese el cateto A: "))
        b = float(input("Ingrese el cateto B: "))

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser valores positivos.")

        tri = TrianguloRectangulo(a, b)

        print(f"\nHipotenusa: {tri.calcular_hipotenusa():.2f}")
        print(f"Área: {tri.calcular_area():.2f}")
        print(f"Perímetro: {tri.calcular_perimetro():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":  
    main()
