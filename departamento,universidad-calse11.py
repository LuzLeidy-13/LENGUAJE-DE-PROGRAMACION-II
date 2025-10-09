class Departamento:
    def __init__(self,nombre):
        self.nombre = nombre

class Universidad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.departamento=[]

    def agregar_departamento(self,departamento):
        self.departamento.append(departamento)

    def mostrar_departamentos(self):
        print(f"Universidad: {self.nombre}")
        print("Departamentos:")
        for dep in self.departamento:
            print(f"- {dep.nombre}")

dep1 = Departamento("ingenieria estadistica")
dep2 = Departamento("informatica")

uni = Universidad("universidad nacional del altiplano")
uni.agregar_departamento(dep1)
uni.agregar_departamento(dep2)

print(uni.departamento)
                  
