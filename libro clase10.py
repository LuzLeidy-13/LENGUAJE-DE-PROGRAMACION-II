import gc
class Libro:
    def __init__(self, titulo,autor,anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado {self.titulo} {self.autor} años {self.anio}")

    def mostrar_informacion(self):
        print(f"{self.titulo} fue escrito por {self.autor} en {self.anio}")

    def __del__(self):
        print(f"libro eliminado {self.titulo}")

libros_datos = [("cien años de soledad","grabriel marcia marquez", 1967),
                     ("don quijote de la mancha","miguel de cervante",1605)]

biblioteca = []

for datos in libros_datos:
    libro = Libro(*datos)  
    libro.mostrar_informacion()
    biblioteca.append(libro)

biblioteca.clear()
del libro
gc.collect()
print("fin de programa")
