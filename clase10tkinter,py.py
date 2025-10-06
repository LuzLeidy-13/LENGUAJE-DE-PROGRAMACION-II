
import tkinter as tk
import gc

class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        print(f"Estudiante registrado: {self.nombre}, {self.edad} años, {self.carrera}")

    def mostrar_informacion(self):
        return f"{self.nombre} estudia {self.carrera} y tiene {self.edad} años"

    def __del__(self):
        print(f"Estudiante eliminado: {self.nombre}")


grupo = []


def agregar_estudiante():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    carrera = entry_carrera.get()

    if nombre and edad.isdigit() and carrera:
        estudiante = Estudiante(nombre, int(edad), carrera)
        grupo.append(estudiante)
        lista.insert(tk.END, estudiante.mostrar_informacion())
        entry_nombre.delete(0, tk.END)
        entry_edad.delete(0, tk.END)
        entry_carrera.delete(0, tk.END)


def eliminar_estudiantes():
    grupo.clear()
    gc.collect()
    lista.delete(0, tk.END)
    lista.insert(tk.END, "Estudiantes eliminados")


# Ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Estudiantes")
ventana.configure(bg="lightblue")   # color de fondo de la ventana

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:", bg="lightblue", fg="darkblue", font=("Arial", 10, "bold")).grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana, bg="white", fg="black")
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Edad:", bg="lightblue", fg="darkblue", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
entry_edad = tk.Entry(ventana, bg="white", fg="black")
entry_edad.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Carrera:", bg="lightblue", fg="darkblue", font=("Arial", 10, "bold")).grid(row=2, column=0, padx=5, pady=5)
entry_carrera = tk.Entry(ventana, bg="white", fg="black")
entry_carrera.grid(row=2, column=1, padx=5, pady=5)

# Botones con colores
btn_agregar = tk.Button(ventana, text="Agregar Estudiante", command=agregar_estudiante,
                        bg="green", fg="white", activebackground="darkgreen")
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar Estudiantes", command=eliminar_estudiantes,
                         bg="red", fg="white", activebackground="darkred")
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

# Listbox con colores
lista = tk.Listbox(ventana, width=50, height=10, bg="white", fg="black",
                   selectbackground="yellow", selectforeground="black")
lista.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
print("fin de programa")
