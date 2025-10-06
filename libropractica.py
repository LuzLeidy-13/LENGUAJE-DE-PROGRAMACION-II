class Libro:
    def _init_(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro '{self.titulo}' de {self.autor} creado.")

    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")

    def _del_(self):
        print(f"Libro '{self.titulo}' eliminado de la biblioteca.")

titulo = input("Ingrese el título del libro: ")
autor = input("Ingrese el autor del libro: ")
anio = int(input("Ingrese el año de publicación: "))

libro1 = Libro(titulo, autor, anio)
libro1.mostrar_info()

del libro

try:
    libro1.mostrar_info()
except NameError:
    print("El objeto ya no existe")
