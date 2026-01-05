class MetodoDePago:
    def pagar(self, monto):
        print(f"Pagando {monto} soles con un método de pago genérico.")

class TarjetaDeCredito(MetodoDePago):
    def pagar(self, monto):
        print(f"Pagando {monto} soles con Tarjeta de Crédito.")


class Yape(MetodoDePago):
    def pagar(self, monto):
        print(f"Pagando {monto} soles con Yape.")


class Plin(MetodoDePago):
    def pagar(self, monto):
        print(f"Pagando {monto} soles con Plin.")


class Efectivo(MetodoDePago):
    def pagar(self, monto):
        print(f"Pagando {monto} soles en Efectivo.")

metodos = [TarjetaDeCredito(),Yape(),Plin(),Efectivo()]

for metodo in metodos:
    metodo.pagar(50)
