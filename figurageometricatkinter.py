from typing import TypeVar, Generic
import tkinter as tk
import math

T = TypeVar("T", int, float)

# ---------------------------------
# CLASE GENÉRICA
# ---------------------------------
class FigurasGeometricas(Generic[T]):
    def area(self) -> T:
        raise NotImplementedError("Implementar en subclase")

    def perimetro(self) -> T:
        raise NotImplementedError("Implementar en subclase")


# ---------------------------------
# RECTÁNGULO
# ---------------------------------
class Rectangulo(FigurasGeometricas[T]):
    def __init__(self, base: T, altura: T):
        self.base = base
        self.altura = altura

    def area(self) -> T:
        return self.base * self.altura

    def perimetro(self) -> T:
        return 2 * (self.base + self.altura)


# ---------------------------------
# CÍRCULO
# ---------------------------------
class Circulo(FigurasGeometricas[T]):
    def __init__(self, radio: T):
        self.radio = radio

    def area(self) -> T:
        return math.pi * (self.radio ** 2)

    def perimetro(self) -> T:
        return 2 * math.pi * self.radio


# ============================================
#          INTERFAZ GRÁFICA MEJORADA
# ============================================
class VentanaFiguras:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Figuras Geométricas")
        self.ventana.geometry("700x520")
        self.ventana.resizable(False, False)

        # -------------------------
        # CANVAS
        # -------------------------
        self.canvas = tk.Canvas(self.ventana, width=420, height=420, bg="white", bd=3, relief="groove")
        self.canvas.place(x=20, y=20)

        # -------------------------
        # TÍTULO EXPLICATIVO
        # -------------------------
        titulo = tk.Label(
            self.ventana,
            text="Ingresa las medidas dependiendo de la figura:",
            font=("Arial", 12, "bold"),
            fg="#333"
        )
        titulo.place(x=460, y=20)

        # -------------------------
        # LABEL: BASE / RADIO
        # -------------------------
        tk.Label(self.ventana, text="1) Base (Rectángulo) o Radio (Círculo):",
                 font=("Arial", 11)).place(x=460, y=60)

        self.entry1 = tk.Entry(self.ventana, font=("Arial", 12), width=15)
        self.entry1.place(x=460, y=90)

        # Placeholder
        self.entry1.insert(0, "Ej: 10")

        # -------------------------
        # LABEL: ALTURA
        # -------------------------
        tk.Label(self.ventana, text="2) Altura (Solo para Rectángulo):",
                 font=("Arial", 11)).place(x=460, y=140)

        self.entry2 = tk.Entry(self.ventana, font=("Arial", 12), width=15)
        self.entry2.place(x=460, y=170)
        self.entry2.insert(0, "Ej: 5")

        # -------------------------
        # BOTONES
        # -------------------------
        tk.Button(self.ventana,
                  text="Dibujar Rectángulo",
                  bg="#9932cc", fg="white",
                  font=("Arial", 12, "bold"),
                  width=18,
                  command=self.dibujar_rectangulo).place(x=460, y=230)

        tk.Button(self.ventana,
                  text="Dibujar Círculo",
                  bg="#00bfff", fg="white",
                  font=("Arial", 12, "bold"),
                  width=18,
                  command=self.dibujar_circulo).place(x=460, y=280)

        # -------------------------
        # RESULTADO
        # -------------------------
        self.resultado = tk.StringVar()
        tk.Label(self.ventana, text="Resultado:", font=("Arial", 12, "bold")).place(x=460, y=340)

        tk.Label(self.ventana,
                 textvariable=self.resultado,
                 font=("Arial", 12),
                 fg="darkgreen",
                 wraplength=200,
                 justify="left").place(x=460, y=370)

        self.ventana.mainloop()

    # ---------------------------------------
    # DIBUJAR RECTÁNGULO
    # ---------------------------------------
    def dibujar_rectangulo(self):
        try:
            base = float(self.entry1.get())
            altura = float(self.entry2.get())

            rect = Rectangulo(base, altura)

            area = rect.area()
            per = rect.perimetro()

            self.resultado.set(f"Área: {area:.2f}\nPerímetro: {per:.2f}")

            self.canvas.delete("all")

            scale = 4
            w = base * scale
            h = altura * scale

            self.canvas.create_rectangle(50, 50, 50 + w, 50 + h,
                                         fill="#ff69b4", outline="black", width=3)

        except:
            self.resultado.set("Error: ingresa valores numéricos válidos.")

    # ---------------------------------------
    # DIBUJAR CÍRCULO
    # ---------------------------------------
    def dibujar_circulo(self):
        try:
            radio = float(self.entry1.get())

            circ = Circulo(radio)

            area = circ.area()
            per = circ.perimetro()

            self.resultado.set(f"Área: {area:.2f}\nPerímetro: {per:.2f}")

            self.canvas.delete("all")

            scale = 4
            r = radio * scale

            self.canvas.create_oval(200 - r, 200 - r, 200 + r, 200 + r,
                                    fill="#7fff00", outline="black", width=3)

        except:
            self.resultado.set("Error: ingresa valores numéricos válidos.")


# Ejecutar
VentanaFiguras()
