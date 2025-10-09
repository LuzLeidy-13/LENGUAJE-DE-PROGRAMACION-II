import math
class Rectangulo:
    def __init__(self,base,altura):
        self.__base = base #atributo privado
        self.__altura = altura 
       
    def get_base(self):
        return self.__base

    def get_altura(self):
        return self.__altura
    
    def set_base(self,nueva_base):
        if nueva_base > 0:
            self.__base = nueva_base
        else:
            print("no valida")

    def set_altura(self,nueva_altura):
        self.__altura = nueva_altura
        return self.__altura

    def calcular_area(self):
         return self.__base*self.__altura
 
        

rectangulo = Rectangulo()
print("area dl circulo ",round (circulo.calcular_area(),2))


f
