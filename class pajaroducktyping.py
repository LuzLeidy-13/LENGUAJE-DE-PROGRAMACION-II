class Pajaro:
    def volar(self):
        print("el pajaro vuela ")

class Avion:
    def volar(self0):
        print("el avion vuela")

def hacer_volar(obj):
    obj.volar()

hacer_volar(Pajaro())
hacer_volar(Avion())
