import gc
class Estudiante:
    def __init__(self, nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado {self.nombre} {self.edad} años {self.carrera}")

    def mostrar_informacion(self):
        print(f"{self.nombre} estudia {self.carrera} y tiene {self.edad}")

    def __del__(self):
        print(f"estudiante eliminado {self.nombre}")

datos_estudiantes = [("ana",20, "medicina"),
                     ("luis",22,"arquitectura"),
                     ("carla",19,"arquitectura"),
                     ("luz",20,"estadistica"),
                     ("nayelin",19,"informatica")]

grupo = []

for datos in datos_estudiantes:
    estudiante = Estudiante(*datos)  
    estudiante.mostrar_informacion()
    grupo.append(estudiante)

grupo.clear()
del estudiante
gc.collect()
print("fin de programa")


        
