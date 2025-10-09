import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class SignoZodiacal:
    def __init__(self, dia, mes):
        self.dia = dia
        self.mes = mes

    def fecha_valida(self):
        dias_por_mes = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31
        }
        return self.mes in dias_por_mes and 1 <= self.dia <= dias_por_mes[self.mes]

    def obtener_signo(self):
        if not self.fecha_valida():
            return "Invalido"

        if (self.mes == 3 and self.dia >= 21) or (self.mes == 4 and self.dia <= 19):
            return "Aries"
        elif (self.mes == 4 and self.dia >= 20) or (self.mes == 5 and self.dia <= 20):
            return "Tauro"
        elif (self.mes == 5 and self.dia >= 21) or (self.mes == 6 and self.dia <= 20):
            return "Geminis"
        elif (self.mes == 6 and self.dia >= 21) or (self.mes == 7 and self.dia <= 22):
            return "Cancer"
        elif (self.mes == 7 and self.dia >= 23) or (self.mes == 8 and self.dia <= 22):
            return "Leo"
        elif (self.mes == 8 and self.dia >= 23) or (self.mes == 9 and self.dia <= 22):
            return "Virgo"
        elif (self.mes == 9 and self.dia >= 23) or (self.mes == 10 and self.dia <= 22):
            return "Libra"
        elif (self.mes == 10 and self.dia >= 23) or (self.mes == 11 and self.dia <= 21):
            return "Escorpio"
        elif (self.mes == 11 and self.dia >= 22) or (self.mes == 12 and self.dia <= 21):
            return "Sagitario"
        elif (self.mes == 12 and self.dia >= 22) or (self.mes == 1 and self.dia <= 19):
            return "Capricornio"
        elif (self.mes == 1 and self.dia >= 20) or (self.mes == 2 and self.dia <= 18):
            return "Acuario"
        elif (self.mes == 2 and self.dia >= 19) or (self.mes == 3 and self.dia <= 20):
            return "Piscis"
        else:
            return "Invalido"


# --- Interfaz gráfica ---
def calcular_signo():
    try:
        dia = int(entry_dia.get())
        mes = int(entry_mes.get())
        signo = SignoZodiacal(dia, mes).obtener_signo()

        if signo == "Invalido":
            messagebox.showerror("Error", "Fecha inválida")
            return

        resultado.set(f"Tu signo zodiacal es: {signo}")

        # Mostrar imagen correspondiente
        try:
            img = Image.open(f"imagenes/{signo.lower()}.png")
            img = img.resize((120, 120))  # redimensionar
            img_tk = ImageTk.PhotoImage(img)
            label_imagen.config(image=img_tk)
            label_imagen.image = img_tk  # mantener referencia
        except FileNotFoundError:
            messagebox.showwarning("Aviso", f"No se encontró la imagen de {signo}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese números válidos.")


# Ventana principal
ventana = tk.Tk()
ventana.title("Calculadora de Signo Zodiacal")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Etiquetas y entradas
tk.Label(ventana, text="Día de nacimiento:").pack(pady=5)
entry_dia = tk.Entry(ventana)
entry_dia.pack()

tk.Label(ventana, text="Mes de nacimiento (número):").pack(pady=5)
entry_mes = tk.Entry(ventana)
entry_mes.pack()

# Botón
btn = tk.Button(ventana, text="Calcular Signo", command=calcular_signo)
btn.pack(pady=10)

# Resultado
resultado = tk.StringVar()
lbl_resultado = tk.Label(ventana, textvariable=resultado, font=("Arial", 12, "bold"), fg="blue")
lbl_resultado.pack(pady=10)

# Imagen del signo
label_imagen = tk.Label(ventana)
label_imagen.pack(pady=10)

# Iniciar ventana
ventana.mainloop()

