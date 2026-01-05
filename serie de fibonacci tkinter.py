import tkinter as tk
from tkinter import messagebox

def fibonacci(n):
    a, b = 0, 1
    resultado = str(a) + " "
    
    if n > 1:
        resultado += str(b) + " "
    
    for _ in range(2, n):
        c = a + b
        resultado += str(c) + " "
        a, b = b, c
    
    return resultado

def calcular():
    try:
        n = int(entrada.get())

        if n <= 0:
            raise ValueError("Debe ingresar un número entero positivo.")

        serie = fibonacci(n)
        resultado_var.set(serie)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))
    except Exception as e:
        messagebox.showerror("Error inesperado", str(e))

# ------------------------- INTERFAZ TKINTER -------------------------

ventana = tk.Tk()
ventana.title("Serie de Fibonacci")
ventana.geometry("400x250")

tk.Label(ventana, text="Ingrese número de términos:", font=("Arial", 12)).pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack()

btn = tk.Button(ventana, text="Generar Serie", font=("Arial", 12), command=calcular)
btn.pack(pady=15)

resultado_var = tk.StringVar()

tk.Label(ventana, text="Resultado:", font=("Arial", 12)).pack()
tk.Label(ventana, textvariable=resultado_var, font=("Arial", 12), wraplength=350).pack()

ventana.mainloop()
