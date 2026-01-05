class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible para préstamo.")

    def devolver(self):
        self.disponible = True
        print(f"El libro '{self.titulo}' ha sido devuelto.")


class Prestamo:
    def __init__(self, libro, fecha_prestamo):
        self.libro = libro
        self.fecha_prestamo = fecha_prestamo
        self.devuelto = False

    def marcar_devolucion(self):
        self.devuelto = True
        self.libro.devolver()


class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.prestamos = []  

    def realizar_prestamo(self, libro, fecha):
        if libro.disponible: 
            libro.prestar()
            nuevo_prestamo = Prestamo(libro, fecha)
            self.prestamos.append(nuevo_prestamo)  #
        else:
            print("No se puede realizar el préstamo del libro, NO DISPONIBLE")

    def mostrar_prestamos(self):
        print(f"\nPréstamos de {self.nombre}:")
        if not self.prestamos:
            print("No tiene préstamos registrados.")
        for p in self.prestamos:
            estado = "Devuelto" if p.devuelto else "Pendiente"
            print(f"- {p.libro.titulo} ({estado}) - Fecha: {p.fecha_prestamo}")


def main():
    libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "987654")
    libro2 = Libro("Cien años de soledad", "Gabriel García Márquez", "123456")

    usuario1 = Usuario("Juan López", "01254")

    usuario1.realizar_prestamo(libro1, "2025-10-13")
    usuario1.mostrar_prestamos()

    usuario1.prestamos[0].marcar_devolucion()
    usuario1.mostrar_prestamos()


if __name__ == "__main__":
    main()
