from typing import TypeVar, Generic
import math

T = TypeVar("T", int, float)


class FigurasGeometricas(Generic[T]):
    def area(self) -> T:
        raise NotImplementedError("Este método debe ser implementado en la subclase")

    def perimetro(self) -> T:
        raise NotImplementedError("Este método debe ser implementado en la subclase")


class Rectangulo(FigurasGeometricas[T]):
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura

    def area(self) -> T:
        return self.base * self.altura

    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)



class Circulo(FigurasGeometricas[T]):
    def __init__(self, radio: T):
        self.radio = radio

    def area(self) -> T:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> T:
        return 2 * math.pi * self.radio



def main():
    rect = Rectangulo(10, 5)
    circ = Circulo(7)

    print("RECTÁNGULO")
    print("Área:", rect.area())
    print("Perímetro:", rect.perimetro())

    print("\nCÍRCULO")
    print("Área:", circ.area())
    print("Perímetro:", circ.perimetro())


if __name__ == "__main__":
    main()
