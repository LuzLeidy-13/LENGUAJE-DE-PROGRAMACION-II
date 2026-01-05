from typing import TypeVar, Generic
import math

T = TypeVar("T", int, float)

class TrianguloRectangulo(Generic[T]):
    def _init_(self, catetoa: T, catetob: T):
        self.catetoa = float(catetoa)
        self.catetob = float(catetob)

    def hipotenusa(self) -> float:
        return math.sqrt(self.catetoa * 2 + self.catetob * 2)

    def area(self) -> float:
        return (self.catetoa * self.catetob) / 2

    def perimetro(self) -> float:
        return (self.catetoa + self.catetob + self.hipotenusa())


def main():
    try:
        c1 = float(input("Ingrese el cateto A: "))
        c2 = float(input("Ingrese el cateto B: "))

        if c1 <= 0 or c2 <= 0:
            raise ValueError("Los catetos deben ser números positivos.")

        tri = TrianguloRectangulo(c1, c2)

        print(f"Hipotenusa: {tri.hipotenusa():.2f}")
        print(f"Área: {tri.area():.2f}")
        print(f"Perímetro: {tri.perimetro():.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()