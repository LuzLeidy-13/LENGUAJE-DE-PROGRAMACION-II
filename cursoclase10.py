import gc
class   Curso:
    def __init__(self,nombre ,codigo,profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        print(f"\n nombre del curso {self.nombre}  {self.codigo}  {self.codigo}")

    def mostrar_informacion(self):
        print(f"{self.nombre} {self.codigo}  {self.profesor}")

    def __del__(self):
        print(f"producto eliminado {self.nombre}")



curso_datos = [("lenuaje de programacion II ","EST301","LEONEL"),
               ("PROGRAMACION NUMERICA","EST207","fred")]

loscursos = []
for datos in curso_datos:
    curso = Curso(*datos)  
    curso.mostrar_informacion()
    loscursos.append(curso)

loscursos.clear()
del curso
gc.collect()
print("fin de programa")
