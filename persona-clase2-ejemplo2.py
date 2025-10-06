class persona:
    def __init__(self,nombre,edad):
       self.nombre = nombre
       self.edad = edad

    def es_mayor_de_edad(self):
        if self.edad >=18:
            return True
        else :
            return False
persona = persona("maria",15)

if persona.es_mayor_de_edad():
    print(f"{persona.nombre} es mayor de edad")
else:
    print(f"{persona.nombre} es menor de edad")
