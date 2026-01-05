class Animal:
    def hacer_sonido(self):
        print("sonido generico")

class Perro(Animal):
    def hacer_sonido(self):
        print("GUaa")

class Gato(Animal):
    def hacer_sonido(self):
        print("MIauu")

animales =[Perro(),Gato(),Animal()]
for animal in animales:
    animal.hacer_sonido()
