import math
class Comida:
    def __init__(self,proteinas,carbohidratos,grasas):
        self.proteinas = proteinas
        self.carbohidratos = carbohidratos
        self.grasas = grasas
        print("objeto comida creado")
        print (f"{self.proteinas}g.{self.carbohidratos}g.{self.grasas}g.")
        
    def calcular_calorias(self):
         calorias = (self.proteinas*4 + self.carbohidratos*4 + self.grasas*9)
         return calorias

    def mostrar_informacion(self):
        print("informacion nutricioanl")
        print(f"proteinas{self.proteinas}g.")
        print(f"carbohidratos{self.carbohidratos}g.")
        print(f"grasas{self.grasas}g.")
        print(f"calorias totales :{self.calcular_calorias()}kcal")



almuerzo = Comida(proteinas=30, carbohidratos=50 ,grasas=20)
almuerzo.mostrar_informacion

del almuerzo

try:
    almuerzo.mostrar_informacion()

except NameError:
    print(f"el objeto ya no existe ")

    
