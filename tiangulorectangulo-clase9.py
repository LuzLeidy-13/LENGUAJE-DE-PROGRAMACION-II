import math
class TrianguloRectangulo:
    def __init__(self,cateto_a,cateto_b): # constructores
        self.cateto_a = cateto_a
        self.cateto_b = cateto_b

    def calcular_hipotenusa(self):
        hipotenusa = math.sqrt(self.cateto_a**2+ self.cateto_b**2)
        return hipotenusa

    def __del__(self):
        print("objeto triangulo rectangulo")

def main():
    try:
        cateto1 = float (input("ingrese el valor del primer cateto "))
        cateto2 = float (input("ingrese el vslor del segundo cateto"))

        triangulo = TrianguloRectangulo(cateto1,cateto2)
        resultado = triangulo.calcular_hipotenusa()

        print(f"la hipotenusa del triangulo es {resultado}")
        
except NameError:
        
if __name__=="__main__":
    main()
