
import tkinter as tk
import gc

class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        print(f"Libro registrado: {self.titulo}, {self.autor}, {self.anio}")

    def mostrar_informacion(self):
        return f"'{self.titulo}' fue escrito por {self.autor} en {self.anio}"

    def __del__(self):
        print(f"Libro eliminado: {self.titulo}")


biblioteca = []


def agregar_libro():
    titulo = entry_titulo.get()
    autor = entry_autor.get()
    anio = entry_anio.get()

    if titulo and autor and anio.isdigit():
        libro = Libro(titulo, autor, int(anio))
        biblioteca.append(libro)
        lista.insert(tk.END, libro.mostrar_informacion())
        # limpiar entradas
        entry_titulo.delete(0, tk.END)
        entry_autor.delete(0, tk.END)
        entry_anio.delete(0, tk.END)


def eliminar_libros():
    biblioteca.clear()
    gc.collect()
    lista.delete(0, tk.END)
    lista.insert(tk.END, "Libros eliminados")


# Ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca - Gestión de Libros")
ventana.configure(bg="lightyellow")

# Etiquetas y entradas
tk.Label(ventana, text="Título:", bg="lightyellow", fg="brown", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
entry_titulo = tk.Entry(ventana, bg="white", fg="black")
entry_titulo.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Autor:", bg="lightyellow", fg="brown", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
entry_autor = tk.Entry(ventana, bg="white", fg="black")
entry_autor.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Año:", bg="lightyellow", fg="brown", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)
entry_anio = tk.Entry(ventana, bg="white", fg="black")
entry_anio.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Libro", command=agregar_libro,
                        bg="green", fg="white", activebackground="darkgreen")
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar Libros", command=eliminar_libros,
                         bg="red", fg="white", activebackground="darkred")
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

# Listbox para mostrar los libros
lista = tk.Listbox(ventana, width=60, height=10, bg="white", fg="black",
                   selectbackground="lightblue", selectforeground="black")
lista.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
print("fin de programa")
