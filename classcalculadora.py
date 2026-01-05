from typing import TypeVar, Generic
import tkinter as tk

T = TypeVar("T", int, float)

# -----------------------------------------
#          CLASE CALCULADORA
# -----------------------------------------
class Calculadora(Generic[T]):
    def __init__(self, a: T, b: T):  
        try:
            self.a = a
            self.b = b
        except Exception as e:
            raise TypeError(f"error al asignar valores: {e}")

    def sumar(self) -> T:
        try:
            return self.a + self.b
        except Exception as e:
            raise TypeError(f"error al sumar: {e}")
    
    def restar(self) -> T:
        try:
            return self.a - self.b
        except Exception as e:
            raise TypeError(f"error al restar: {e}")
      
    def multiplicar(self) -> T:
        try:
            return self.a * self.b
        except Exception as e:
            raise TypeError(f"error al multiplicar: {e}")
    
    def dividir(self) -> T:
        try:
            if self.b == 0:
                raise ValueError("no se puede dividir entre cero")
            return self.a / self.b
        except Exception as e:
            raise TypeError(f"error al dividir: {e}")

# -----------------------------------------
#          FUNCIÓN DE OPERACIÓN
# -----------------------------------------
def operar(tipo):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())

        calc = Calculadora(a, b)

        if tipo == "sumar":
            r = calc.sumar()
        elif tipo == "restar":
            r = calc.restar()
        elif tipo == "multiplicar":
            r = calc.multiplicar()
        elif tipo == "dividir":
            r = calc.dividir()

        resultado.set(f"Resultado: {r}")

    except Exception as e:
        resultado.set(f"Error: {str(e)}")

# -----------------------------------------
#          INTERFAZ GRÁFICA TKINTER
# -----------------------------------------
def main():
    global entry_a, entry_b, resultado

    ventana = tk.Tk()
    ventana.title("Calculadora Tkinter")
    ventana.geometry("450x260")
    ventana.resizable(False, False)
    
    # Fondo MORADO
    ventana.config(bg="#6a0dad")  # morado oscuro

    tk.Label(ventana, text="Número A:", font=("Arial", 11), bg="#6a0dad", fg="white").pack(pady=5)
    entry_a = tk.Entry(ventana, font=("Arial", 12))
    entry_a.pack()

    tk.Label(ventana, text="Número B:", font=("Arial", 11), bg="#6a0dad", fg="white").pack(pady=5)
    entry_b = tk.Entry(ventana, font=("Arial", 12))
    entry_b.pack()

    # -----------------------------------------
    #       BOTONES EN UNA SOLA FILA
    # -----------------------------------------
    frame_botones = tk.Frame(ventana, bg="#6a0dad")
    frame_botones.pack(pady=10)

    tk.Button(frame_botones, text="SUMAR", width=10, command=lambda: operar("sumar")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="RESTAR", width=10, command=lambda: operar("restar")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="MULTIPLICAR", width=12, command=lambda: operar("multiplicar")).pack(side="left", padx=5)
    tk.Button(frame_botones, text="DIVIDIR", width=10, command=lambda: operar("dividir")).pack(side="left", padx=5)

    resultado = tk.StringVar()
    tk.Label(ventana, textvariable=resultado, font=("Arial", 14), fg="yellow", bg="#6a0dad").pack(pady=15)

    ventana.mainloop()

# -----------------------------------------
#          CORRECCIÓN DEL ERROR
# -----------------------------------------
if __name__ == "__main__":
    main()   # ← ESTA LÍNEA DEBE ESTAR INDENTADA
