class Vehiculo:
    def iniciar(self):
        print("el vehiculo esta lsito para moverse")

class Coche(Vehiculo):
    def iniciar(self):
        print("el coche arranca y acelera")

class Bicicleta(Vehiculo):
    def iniciar(self):
        print("la bicicleta empieza a pedalear")
class Barco(Vehiculo):
    def iniciar(self):
        print("el barco enciende el motor y zarpa")

vehiculos = [Coche(),Bicicleta(),Barco()]

for v in vehiculos:
    v.iniciar()
    
