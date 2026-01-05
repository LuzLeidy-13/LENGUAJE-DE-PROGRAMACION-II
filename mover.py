class Pajaro:
    def mover(self):
        print("el pajaro vuela")

class Pes:
    def mover(self):
        print("el pes nada")

class Persona:
    def mover(self):
        print("la persona camina")

def desplazar(objeto):
    objeto.mover()
objetos = [Pajaro(),Pes(),Persona()]
for objeto in objetos:
    desplazar(objeto)
