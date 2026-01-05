class Factorial:
    def __init__(self, numero):
        self.__numero = numero

    def calcular (self):
        if self.__numero < 0:
            return "el factorial no esta definido para numeros negativos"
        resultado = 1 
        for i in range (1,self.__numero+1):
            resultado *= i
        return resultado

    def mostrar_resultado(self):
        resultado = self.calcular()
        print (f"El factorial de {self.__numero} es:{resultado} ")

mifactorial = Factorial(5)
mifactorial.mostrar_resultado()
    
            
