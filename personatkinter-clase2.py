import tkinter as tk
from tkinter import messagebox

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def es_mayor_de_edad(self):
        return self.edad >= 18


def comprobar():
    nombre = nombre_var.get().strip()
    edad_str = edad_var.get().strip()

    if not nombre:
        messagebox.showwarning("Falta nombre", "Por favor ingresa el nombre.")
        return

    try:
        edad = int(edad_str)
        if edad < 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Edad inválida", "La edad debe ser un número entero no negativo.")
        return

    p = Persona(nombre, edad)
    if p.es_mayor_de_edad():
        resultado_label.config(text=f"{p.nombre} es mayor de edad", fg="green")
    else:
        resultado_label.config(text=f"{p.nombre} es menor de edad", fg="red")


def on_enter(event):
    comprobar()


# --- Interfaz ---
root = tk.Tk()
root.title("Comprobador de edad")
root.geometry("400x300")
root.resizable(False, False)
root.configure(padx=12, pady=12)

# Variables
nombre_var = tk.StringVar()
edad_var = tk.StringVar()

# Widgets
tk.Label(root, text="Nombre:", anchor="w").pack(fill="x", pady=(0,4))
nombre_entry = tk.Entry(root, textvariable=nombre_var, font=("Arial", 12))
nombre_entry.pack(fill="x", pady=(0,8))

tk.Label(root, text="Edad:", anchor="w").pack(fill="x", pady=(0,4))
edad_entry = tk.Entry(root, textvariable=edad_var, font=("Arial", 12))
edad_entry.pack(fill="x", pady=(0,8))

btn_comprobar = tk.Button(root, text="Comprobar", command=comprobar, font=("Arial", 11, "bold"))
btn_comprobar.pack(pady=(6,8), ipadx=6, ipady=4)

resultado_label = tk.Label(root, text="", font=("Arial", 12))
resultado_label.pack(pady=(4,0))

# Permitir pulsar Enter para comprobar
root.bind("<Return>", on_enter)

# Poner el foco inicialmente en el campo nombre
nombre_entry.focus()

root.mainloop()
