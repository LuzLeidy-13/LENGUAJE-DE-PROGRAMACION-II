class numeros:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.contador = 0
    def generarnumeros (self):
        print(" imprime numeros ")
        while self.contador <= self.cantidad:
            print(self.contador)
            self.contador+=1


def main():
    minumero = numeros(10)
    minumero.generarnumeros()
if __name__=="__main__":
    main()
