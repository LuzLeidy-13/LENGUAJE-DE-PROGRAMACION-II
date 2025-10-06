class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        print(f"Bienvenido {self.titular}, cuenta creada con saldo {self.saldo}.")

    def depositar(self, monto):
        self.saldo += monto
        print(f"Depósito de {monto} realizado. Saldo actual: {self.saldo}")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
            print(f"Retiro de {monto} realizado. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def __del__(self):
        print(f"Cuenta de {self.titular} cerrada.")

titular = input("Ingrese el nombre del titular: ")
saldo_inicial = float(input("Ingrese el saldo inicial: "))

cuenta1 = CuentaBancaria(titular, saldo_inicial)

deposito = float(input("Ingrese el monto a depositar: "))
cuenta1.depositar(deposito)

retiro = float(input("Ingrese el monto a retirar: "))
cuenta1.retirar(retiro)

del cuenta1

try:
    cuenta1.depositar(100)
except NameError:
    print("El objeto ya no existe")
