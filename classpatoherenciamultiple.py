class Nadador: #clase base1
    def nadar(self):
        print("nadando en el agua")

class Volar:
    def volar(self):
        print("volando por el aire")

class Pato(Nadador,Volar):
    def graznar(self):
        print("cuac")

pato=Pato()
pato.nadar()
pato.volar()
pato.graznar()
    
