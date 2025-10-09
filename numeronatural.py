class NumeroNatural:
    def __init__(self, valor):
        self.valor = valor

    def mostrar(self):
        if self.valor == 0:
            print(f"El: {self.valor} es número nulo")
        elif self.valor % 2 == 0:
            print(f"El: {self.valor} es número par")
        else:
            print(f"El: {self.valor} es número impar")
        print("*-" * 30)

def main():
    i = 0
    while i <= 10:
        numero = NumeroNatural(i)
        numero.mostrar()
        i += 1

if __name__ == "__main__":
    main()
