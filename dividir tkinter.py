import tkinter as tk
from tkinter import messagebox

class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def dividir(self):
        try:
            resultado = self.a / self.b
            return resultado
        except ZeroDivisionError:
            return "Error: No se puede dividir entre cero"
        except Exception as e:
            return f"Ocurrió un error {e}"
        finally:
            print("Operación finalizada")

# --- Interfaz Gráfica ---

def calcular():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        operacion = Division(a, b)
        resultado = operacion.dividir()
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Debe ingresar números válidos")

# Ventana
ventana = tk.Tk()
ventana.title("División con Tkinter")
ventana.geometry("280x200")
ventana.config(bg="#e3e3e3")

# Etiquetas y campos
tk.Label(ventana, text="Ingrese a:", bg="#e3e3e3").pack()
entry_a = tk.Entry(ventana)
entry_a.pack()

tk.Label(ventana, text="Ingrese b:", bg="#e3e3e3").pack()
entry_b = tk.Entry(ventana)
entry_b.pack()

# Botón calcular
tk.Button(ventana, text="Dividir", command=calcular).pack(pady=10)

# Resultado
label_resultado = tk.Label(ventana, text="Resultado: ", bg="#e3e3e3")
label_resultado.pack()

ventana.mainloop()
