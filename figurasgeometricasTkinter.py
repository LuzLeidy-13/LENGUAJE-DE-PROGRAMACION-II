import tkinter as tk
from tkinter import ttk, messagebox
import math

# =========================
# Principio O (Open/Closed)
# =========================
class FiguraGeometrica:
    def calcular_area(self):
        raise NotImplementedError
    
    def calcular_perimetro(self):
        raise NotImplementedError


# =========================
# Principio O y L
# =========================
class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


# =========================
# Principio D
# =========================
class Aplicacion:
    def __init__(self, figura):
        self.figura = figura

    def ejecutar(self):
        return (
            self.figura.calcular_area(),
            self.figura.calcular_perimetro()
        )


# =========================
# Interfaz Gráfica Tkinter
# =========================
class AppGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Figuras Geométricas - SOLID")
        self.root.geometry("350x300")
        self.root.resizable(False, False)

        ttk.Label(root, text="Seleccione la figura:", font=("Arial", 11)).pack(pady=5)

        self.figura_var = tk.StringVar(value="Circulo")
        self.combo = ttk.Combobox(
            root,
            textvariable=self.figura_var,
            values=["Circulo", "Rectangulo"],
            state="readonly"
        )
        self.combo.pack()
        self.combo.bind("<<ComboboxSelected>>", self.actualizar_campos)

        self.frame_campos = ttk.Frame(root)
        self.frame_campos.pack(pady=10)

        self.crear_campos()

        ttk.Button(root, text="Calcular", command=self.calcular).pack(pady=10)

        self.resultado = ttk.Label(root, text="", font=("Arial", 10))
        self.resultado.pack()

    def crear_campos(self):
        for widget in self.frame_campos.winfo_children():
            widget.destroy()

        if self.figura_var.get() == "Circulo":
            ttk.Label(self.frame_campos, text="Radio:").grid(row=0, column=0, padx=5)
            self.radio_entry = ttk.Entry(self.frame_campos)
            self.radio_entry.grid(row=0, column=1)

        else:
            ttk.Label(self.frame_campos, text="Base:").grid(row=0, column=0, padx=5)
            self.base_entry = ttk.Entry(self.frame_campos)
            self.base_entry.grid(row=0, column=1)

            ttk.Label(self.frame_campos, text="Altura:").grid(row=1, column=0, padx=5)
            self.altura_entry = ttk.Entry(self.frame_campos)
            self.altura_entry.grid(row=1, column=1)

    def actualizar_campos(self, event):
        self.crear_campos()

    def calcular(self):
        try:
            if self.figura_var.get() == "Circulo":
                radio = float(self.radio_entry.get())
                figura = Circulo(radio)

            else:
                base = float(self.base_entry.get())
                altura = float(self.altura_entry.get())
                figura = Rectangulo(base, altura)

            app = Aplicacion(figura)
            area, perimetro = app.ejecutar()

            self.resultado.config(
                text=f"Área: {area:.2f}\nPerímetro: {perimetro:.2f}"
            )

        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")



# =========================
# Ejecución
# =========================
if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
