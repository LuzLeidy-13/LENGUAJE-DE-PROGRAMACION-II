class sumanaturales:
    def __init__(self,limite):
        self.limite = limite
        self.suma =0

    def calcularsuma(self):
        for i in range(1,self.limite+1):
            self.suma = self.suma + i
        return self.suma

def main ():

    misuma = sumanaturales(10)
    resultado = misuma.calcularsuma()
    print(f"la suma de los primeros{misuma.limite}numeros naturales es {resultado}")

if __name__=="__main__":
    main()

