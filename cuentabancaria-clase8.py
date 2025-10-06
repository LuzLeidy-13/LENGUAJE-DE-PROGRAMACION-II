class Cuentabancaria:
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo

    def mostrar(self):
        print(f"titular: {self.titular} saldo:$ {self.saldo:.2f}")

    def __sub__(self):
        if isinstance(cantidad,(int,float)):
            if cantidad <= self.saldo:
                return Cuentabancaria(self.titular, self.saldo_cantidad)
            else:
                print("fondo insuficiente")
                return self
        else:
            print("operador no  valido")
            return self

cuenta1 = Cuentabancaria("luis",1000)
cuenta1.mostrar()

cuenta2 = cuenta1 - 250
cuenta2.mostrar()

cuenta3 = cuenta2 - 1000
cuenta3.mostrar()

