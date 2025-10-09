import tkinter as tk
from tkinter import messagebox

# Clase Tabla de Multiplicar
class TablaDeMultiplicar:
    def __init__(self, numero):
        self.numero = numero

    def generartabla(self):
        resultados = []
        for i in range(1, 11):
            resultado = self.numero * i
            resultados.append(f"{self.numero} x {i} = {resultado}")
        return resultados

# Función para generar la tabla desde la interfaz
def generar():
    try:
        numero = int(entrada_numero.get())
        tabla = TablaDeMultiplicar(numero)
        resultados = tabla.generartabla()

        # Limpiar resultados previos
        text_resultados.delete("1.0", tk.END)

        # Mostrar resultados en el cuadro de texto
        for linea in resultados:
            text_resultados.insert(tk.END, linea + "\n")
    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa un número válido.")

# Ventana principal
ventana = tk.Tk()
ventana.title("Tabla de Multiplicar")
ventana.geometry("350x400")
ventana.config(bg="#e6e6fa")  # Color lavanda claro

# Etiqueta
etiqueta = tk.Label(ventana, text="Ingrese un número:", font=("Arial", 12), bg="#e6e6fa")
etiqueta.pack(pady=10)

# Entrada
entrada_numero = tk.Entry(ventana, font=("Arial", 12), justify="center")
entrada_numero.pack(pady=5)

# Botón
btn_generar = tk.Button(ventana, text="Generar Tabla", font=("Arial", 12, "bold"), bg="purple", fg="white", command=generar)
btn_generar.pack(pady=10)

# Cuadro de texto para resultados
text_resultados = tk.Text(ventana, font=("Courier", 12), width=25, height=12, bg="white", fg="black")
text_resultados.pack(pady=10)

# Iniciar ventana
ventana.mainloop()

