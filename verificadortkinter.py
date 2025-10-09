import tkinter as tk

# Clase con POO
class VerificadorNumero:
    def __init__(self, numero):
        self.numero = numero

    def esta_dentro(self):
        return 1 <= self.numero <= 10


# Función que conecta la interfaz con la lógica
def verificar():
    try:
        n = int(entry_numero.get())  # Obtener lo que el usuario escribe
        verificador = VerificadorNumero(n)

        if verificador.esta_dentro():
            label_resultado.config(text=f"✅ El número {n} está dentro del rango [1-10].", fg="purple")
        else:
            label_resultado.config(text=f"❌ El número {n} está fuera del rango [1-10].", fg="black")
    except ValueError:
        label_resultado.config(text="⚠️ Ingrese solo números.", fg="purple")


# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Verificador de Números")
ventana.geometry("400x250")
ventana.config(bg="#DCC6E0")  # Fondo color lila

# Etiqueta
label = tk.Label(ventana, text="Ingrese un número entre 1 y 10:", font=("Arial", 12, "bold"), bg="#DCC6E0")
label.pack(pady=10)

# Caja de texto
entry_numero = tk.Entry(ventana, font=("Arial", 15))
entry_numero.pack(pady=5)

# Botón
btn_verificar = tk.Button(ventana, text="Verificar", command=verificar,
                          font=("Arial", 12, "bold"), bg="purple", fg="white")
btn_verificar.pack(pady=10)

# Etiqueta para mostrar el resultado en la misma ventana
label_resultado = tk.Label(ventana, text="", font=("Arial", 15), bg="#DCC6E0")
label_resultado.pack(pady=15)

# Ejecutar
ventana.mainloop()

