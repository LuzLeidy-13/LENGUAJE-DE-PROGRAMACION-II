import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
from PIL import Image, ImageTk

# ---------- VARIABLES GLOBALES ----------
TOTAL_DIA = 0.0
CONTRASENA = "1234"

# ---------- CLASES ----------
class MetodoDePago:
    def __init__(self, titular, dni):
        self.titular = titular
        self.dni = dni

    def pagar(self, monto):
        return f"Pagando {monto:.2f} soles con un método genérico."


class TarjetaDeCredito(MetodoDePago):
    def __init__(self, titular, dni, numero, vencimiento):
        super().__init__(titular, dni)
        self.numero = numero
        self.vencimiento = vencimiento

    def pagar(self, monto):
        return f"Pagando {monto:.2f} soles con Tarjeta de Crédito terminada en {self.numero[-4:]}."


class Yape(MetodoDePago):
    def pagar(self, monto):
        return f"Pagando {monto:.2f} soles con Yape."


class Plin(MetodoDePago):
    def pagar(self, monto):
        return f"Pagando {monto:.2f} soles con Plin."


class Efectivo(MetodoDePago):
    def pagar(self, monto):
        return f"Pagando {monto:.2f} soles en Efectivo."


# ---------- FUNCIÓN PRINCIPAL ----------
def realizar_pago():
    global TOTAL_DIA

    titular = entry_titular.get()
    dni = entry_dni.get()
    monto = entry_monto.get()
    metodo = combo_metodo.get()

    if not titular or not dni or not monto or not metodo:
        messagebox.showwarning("Aviso", "Completa todos los campos.")
        return

    try:
        monto = float(monto)
    except ValueError:
        messagebox.showerror("Error", "El monto debe ser numérico.")
        return

    if metodo == "Tarjeta de Crédito":
        numero = entry_tarjeta.get()
        vencimiento = entry_vencimiento.get()
        if not numero or not vencimiento:
            messagebox.showwarning("Aviso", "Completa los datos de la tarjeta.")
            return
        pago = TarjetaDeCredito(titular, dni, numero, vencimiento)
        imagen = "tarjeta.png"
    elif metodo == "Yape":
        pago = Yape(titular, dni)
        imagen = "yape.png"
    elif metodo == "Plin":
        pago = Plin(titular, dni)
        imagen = "plin.png"
    else:
        pago = Efectivo(titular, dni)
        imagen = "efectivo.png"

    # Actualiza total del día
    TOTAL_DIA += monto
    lbl_total.config(text=f"Total del día: S/ {TOTAL_DIA:.2f}")

    mensaje = pago.pagar(monto)
    lbl_resultado.config(text=mensaje, fg="green")

    # Mostrar imagen
    try:
        img = Image.open(imagen)
        img = img.resize((100, 100))
        img_tk = ImageTk.PhotoImage(img)
        lbl_imagen.config(image=img_tk)
        lbl_imagen.image = img_tk
    except:
        lbl_imagen.config(image="", text="Imagen no encontrada")

    # Crear comprobante
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    voucher = f"""
    -------- COMPROBANTE DE PAGO --------
    Fecha: {fecha}
    Titular: {titular}
    DNI: {dni}
    Método: {metodo}
    Monto: S/ {monto:.2f}
    {mensaje}
    -------------------------------------
    ¡Gracias por su compra!
    """
    text_voucher.config(state="normal")
    text_voucher.delete(1.0, tk.END)
    text_voucher.insert(tk.END, voucher)
    text_voucher.config(state="disabled")


# ---------- LOGIN ----------
def verificar_login():
    clave = entry_pass.get()
    if clave == CONTRASENA:
        login.destroy()
        iniciar_sistema()
    else:
        messagebox.showerror("Acceso denegado", "Contraseña incorrecta.")


# ---------- SISTEMA PRINCIPAL ----------
def iniciar_sistema():
    global entry_titular, entry_dni, entry_monto, combo_metodo, entry_tarjeta, entry_vencimiento
    global lbl_resultado, lbl_imagen, text_voucher, lbl_total

    ventana = tk.Tk()
    ventana.title("Sistema de Pago con Comprobante y Control Diario")
    ventana.geometry("550x750")
    ventana.configure(bg="#e6f2ff")

    tk.Label(ventana, text="SISTEMA DE PAGO", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)

    frame_inputs = tk.Frame(ventana, bg="#e6f2ff")
    frame_inputs.pack(pady=10)

    tk.Label(frame_inputs, text="Titular:", bg="#e6f2ff").grid(row=0, column=0, sticky="e", padx=5, pady=5)
    entry_titular = tk.Entry(frame_inputs, width=30)
    entry_titular.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="DNI:", bg="#e6f2ff").grid(row=1, column=0, sticky="e", padx=5, pady=5)
    entry_dni = tk.Entry(frame_inputs, width=30)
    entry_dni.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Monto (S/):", bg="#e6f2ff").grid(row=2, column=0, sticky="e", padx=5, pady=5)
    entry_monto = tk.Entry(frame_inputs, width=30)
    entry_monto.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Método de pago:", bg="#e6f2ff").grid(row=3, column=0, sticky="e", padx=5, pady=5)
    combo_metodo = ttk.Combobox(frame_inputs, values=["Tarjeta de Crédito", "Yape", "Plin", "Efectivo"], state="readonly", width=27)
    combo_metodo.grid(row=3, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Número de tarjeta:", bg="#e6f2ff").grid(row=4, column=0, sticky="e", padx=5, pady=5)
    entry_tarjeta = tk.Entry(frame_inputs, width=30)
    entry_tarjeta.grid(row=4, column=1, padx=5, pady=5)

    tk.Label(frame_inputs, text="Vencimiento:", bg="#e6f2ff").grid(row=5, column=0, sticky="e", padx=5, pady=5)
    entry_vencimiento = tk.Entry(frame_inputs, width=30)
    entry_vencimiento.grid(row=5, column=1, padx=5, pady=5)

    btn_pagar = tk.Button(ventana, text="Realizar Pago", command=realizar_pago,
                          bg="#2196F3", fg="white", font=("Arial", 11, "bold"))
    btn_pagar.pack(pady=15)

    lbl_resultado = tk.Label(ventana, text="", font=("Arial", 12), bg="#e6f2ff")
    lbl_resultado.pack(pady=5)

    lbl_imagen = tk.Label(ventana, bg="#e6f2ff")
    lbl_imagen.pack(pady=5)

    # Total del día
    lbl_total = tk.Label(ventana, text=f"Total del día: S/ {TOTAL_DIA:.2f}",
                         font=("Arial", 13, "bold"), bg="#e6f2ff", fg="blue")
    lbl_total.pack(pady=10)

    # Área del comprobante
    tk.Label(ventana, text="Comprobante de Pago:", bg="#e6f2ff", font=("Arial", 13, "bold")).pack(pady=5)
    text_voucher = tk.Text(ventana, height=12, width=60, state="disabled", font=("Courier New", 10))
    text_voucher.pack(pady=5)

    ventana.mainloop()


# ---------- INTERFAZ DE LOGIN ----------
login = tk.Tk()
login.title("Acceso al Sistema de Pago")
login.geometry("300x200")
login.configure(bg="#d0e6ff")

tk.Label(login, text="INICIO DE SESIÓN", font=("Arial", 14, "bold"), bg="#d0e6ff").pack(pady=15)
tk.Label(login, text="Contraseña:", bg="#d0e6ff").pack()
entry_pass = tk.Entry(login, show="*", width=20)
entry_pass.pack(pady=5)
tk.Button(login, text="Ingresar", command=verificar_login, bg="#2196F3", fg="white").pack(pady=10)

login.mainloop()
