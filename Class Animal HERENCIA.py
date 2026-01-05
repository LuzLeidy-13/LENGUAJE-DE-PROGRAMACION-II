class Animal: # clase base
    def __init__(self,nombre):
        self.nombre = nombre
    def hacerSonido(self):
        pass

class Perro(Animal):# clase derivada o sub clase
    def hacerSonido(self):
        return("¡Guau!")

class Gato(Animal):
    def hacerSonido(self):
        return("¡Miauu!")
perro = Perro("Rex")
print(f"{perro.nombre} dice {perro.hacerSonido()}")

gato = Gato("terry")
print(f"{gato.nombre} dice {gato.hacerSonido()}")

