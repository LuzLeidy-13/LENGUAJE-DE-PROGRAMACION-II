import tkinter as tk
from tkinter import messagebox

class Fibonaci:
    def __init__(self, cantidad):
        self.cantidad = cantidad
        self.serie = []

    def generarserie(self):
        a, b = 0, 1
        self.serie = []  # Reiniciamos la lista
        for _ in range(self.cantidad):
            self.serie.append(a)
            a, b = b, a + b
        return self.serie

def generar():
    try:
        cantidad = int(entry_cantidad.get())
        if cantidad <= 0:
            messagebox.showwarning("Advertencia", "Ingrese un número mayor que 0")
            return
        
        mifibonaci = Fibonaci(cantidad)
        resultado = mifibonaci.generarserie()
        
        # Mostrar en el cuadro de texto
        text_resultado.delete("1.0", tk.END)
        text_resultado.insert(tk.END, ", ".join(map(str, resultado)))
    except ValueError:
        messagebox.showerror("Error", "Ingrese un número válido")

# Ventana principal
ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("400x300")
ventana.config(bg="#f0f0f0")

# Etiqueta
label = tk.Label(ventana, text="Ingrese la cantidad de números:", font=("Arial", 12), bg="#f0f0f0")
label.pack(pady=10)

# Entrada
entry_cantidad = tk.Entry(ventana, font=("Arial", 12))
entry_cantidad.pack(pady=5)

# Botón
btn_generar = tk.Button(ventana, text="Generar Serie", font=("Arial", 12), command=generar,  bg="#800080",fg="white" )
btn_generar.pack(pady=10)

# Cuadro de texto para resultado
text_resultado = tk.Text(ventana, height=8, width=40, font=("Arial", 11))
text_resultado.pack(pady=10)

ventana.mainloop()
