class verificadornumero:
    def __init__(self, numero):
        self.numero = numero

    def esta_dentro(self):
        return 1 <= self.numero <= 10


def main():
    try:
        n = int(input("Ingrese un número: "))
        verificador = verificadornumero(n)  

        if verificador.esta_dentro():
            print(f" El número {n} está dentro del rango [1-10].")
        else:
            print(f" El número {n} está fuera del rango [1-10].")
    except ValueError:
        print("Ingrese solo numeros.")


if __name__ == "__main__":
    main()
