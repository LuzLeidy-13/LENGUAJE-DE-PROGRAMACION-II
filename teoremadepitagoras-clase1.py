class pitagoras:
    def __init__(self,catetoa,catetob):
        self.catetoa = catetoa
        self.catetob = catetob


    def calcular_hipotenusa(self):
        return (self.catetoa**2 + self.catetob**2)**(1/2)

#solicitar datos al usuario
catetoa = float(input("ingrese catetoa :"))
catetob =  float(input("ingrese catetob :"))

#crear un objeto
Pitagoras=pitagoras(catetoa,catetob)
print("la hipotenusa es",Pitagoras.calcular_hipotenusa())
