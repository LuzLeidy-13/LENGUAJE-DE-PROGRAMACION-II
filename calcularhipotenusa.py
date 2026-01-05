from typing import TypeVar
import math

T = TypeVar("T", int, float)

def calcular_hipotenusa(cateto_a: T, cateto_b: T) -> T:
    return math.sqrt(cateto_a**2 + cateto_b**2)

cateto_a = float(input("Ingrese cateto A: "))
cateto_b = float(input("Ingrese cateto B: "))

print("Hipotenusa:", calcular_hipotenusa(cateto_a, cateto_b))
