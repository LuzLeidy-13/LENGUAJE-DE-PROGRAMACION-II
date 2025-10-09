class fibonacci:
    def __init__(self,cantidad):
        self.cantidad = cantidad
        self.a = 0
        self.b = 1
        self.contador = 0
    def generarserie (self):
        print(" serie de fibonacci")
        while self.contador < self.cantidad:
            print(self.a)
            c = self.a +  self.b
            self.a = self.b
            self.b = c
            self.contador+=1


def main():
    mifibonacci = fibonacci(15)
    mifibonacci.generarserie()
if __name__=="__main__":
    main()
