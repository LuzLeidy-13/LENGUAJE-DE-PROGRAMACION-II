import tkinter as tk
from tkinter import messagebox
import gc

class Curso:
    def __init__(self, nombre, codigo, profesor):
        self.nombre = nombre
        self.codigo = codigo
        self.profesor = profesor
        messagebox.showinfo("Curso Registrado",
                            f"Curso: {self.nombre}\nCódigo: {self.codigo}\nProfesor: {self.profesor}")

    def mostrar_informacion(self):
        return f"{self.nombre} | {self.codigo} | {self.profesor}"

    def __del__(self):
        print(f"Curso eliminado: {self.nombre}")


# Lista de cursos
loscursos = []


def registrar_curso():
    nombre = entry_nombre.get()
    codigo = entry_codigo.get()
    profesor = entry_profesor.get()

    if not nombre or not codigo or not profesor:
        messagebox.showwarning("Error", "Por favor completa todos los campos")
        return

    curso = Curso(nombre, codigo, profesor)
    loscursos.append(curso)
    actualizar_lista()

    # limpiar inputs
    entry_nombre.delete(0, tk.END)
    entry_codigo.delete(0, tk.END)
    entry_profesor.delete(0, tk.END)


def actualizar_lista():
    listbox_cursos.delete(0, tk.END)
    for c in loscursos:
        listbox_cursos.insert(tk.END, c.mostrar_informacion())


def eliminar_cursos():
    loscursos.clear()
    gc.collect()
    listbox_cursos.delete(0, tk.END)
    messagebox.showinfo("Eliminados", "Todos los cursos fueron eliminados")


# Ventana principal
root = tk.Tk()
root.title("Registro de Cursos")

# Etiquetas y entradas
tk.Label(root, text="Nombre del curso:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(root, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Código:").grid(row=1, column=0, padx=5, pady=5)
entry_codigo = tk.Entry(root, width=30)
entry_codigo.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Profesor:").grid(row=2, column=0, padx=5, pady=5)
entry_profesor = tk.Entry(root, width=30)
entry_profesor.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_registrar = tk.Button(root, text="Registrar Curso", command=registrar_curso)
btn_registrar.grid(row=3, column=0, columnspan=2, pady=5)

btn_eliminar = tk.Button(root, text="Eliminar Todos", command=eliminar_cursos)
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

# Listbox para mostrar cursos
listbox_cursos = tk.Listbox(root, width=50)
listbox_cursos.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()

print("Fin de programa")
