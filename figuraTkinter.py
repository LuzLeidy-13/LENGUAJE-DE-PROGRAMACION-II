import math
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# ---------------- CLASES ----------------
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    def area(self):
        return self.lado ** 2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return math.pi * (self.radio ** 2)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return (self.base * self.altura) / 2

# ---------------- FUNCIONES ----------------
def calcular_y_dibujar_3d():
    try:
        lado = float(entry_lado.get())
        radio = float(entry_radio.get())
        base = float(entry_base.get())
        altura = float(entry_altura.get())

        figuras = [
            ("Cuadrado", Cuadrado(lado)),
            ("Círculo", Circulo(radio)),
            ("Triángulo", Triangulo(base, altura))
        ]

        # Limpiar el frame de resultados
        for widget in frame_resultados.winfo_children():
            widget.destroy()

        # Mostrar áreas
        tk.Label(frame_resultados, text="Áreas calculadas:", font=("Arial", 12, "bold"), bg="#d0f0f5").pack()
        for nombre, figura in figuras:
            tk.Label(frame_resultados, text=f"{nombre}: {figura.area():.2f}", font=("Arial", 11), bg="#d0f0f5").pack(anchor="w")

        # Crear figura 3D
        fig = plt.figure(figsize=(6, 4))
        ax = fig.add_subplot(111, projection='3d')
        ax.set_facecolor("#f0f0f0")
        ax.set_title("Figuras Geométricas 3D", fontsize=14, fontweight='bold')

        # --- Dibujar Cuadrado como CUBO ---
        # coordenadas de un cubo centrado
        r = lado / 2
        vertices = [
            # caras del cubo
            [[-r, -r, 0], [r, -r, 0], [r, r, 0], [-r, r, 0]],  # base
            [[-r, -r, lado], [r, -r, lado], [r, r, lado], [-r, r, lado]],  # top
            [[-r, -r, 0], [r, -r, 0], [r, -r, lado], [-r, -r, lado]],
            [[r, -r, 0], [r, r, 0], [r, r, lado], [r, -r, lado]],
            [[r, r, 0], [-r, r, 0], [-r, r, lado], [r, r, lado]],
            [[-r, r, 0], [-r, -r, 0], [-r, -r, lado], [-r, r, lado]]
        ]
        cube = Poly3DCollection(vertices, facecolors="#4CAF50", linewidths=1, edgecolors="black", alpha=0.8)
        ax.add_collection3d(cube)
        ax.text(0, 0, lado + 1, "Cuadrado", color="black", ha="center")

        # --- Dibujar Círculo como CILINDRO ---
        z = [0, radio * 1.5]
        theta = [i * math.pi / 30 for i in range(61)]
        x = [radio * math.cos(t) + 5 for t in theta]
        y = [radio * math.sin(t) + 5 for t in theta]
        for i in range(len(theta) - 1):
            ax.plot([x[i], x[i]], [y[i], y[i]], z, color="#2196F3", alpha=0.6)
        ax.text(5, 0, radio * 1.5 + 1, "Círculo", color="black", ha="center")

        # --- Dibujar Triángulo como PIRÁMIDE ---
        base2 = base / 2
        altura3d = altura
        vertices_piramide = [
            [10 - base2, -base2, 0],
            [10 + base2, -base2, 0],
            [10 + base2, base2, 0],
            [10, 0, altura3d]
        ]
        caras = [
            [vertices_piramide[0], vertices_piramide[1], vertices_piramide[3]],
            [vertices_piramide[1], vertices_piramide[2], vertices_piramide[3]],
            [vertices_piramide[2], vertices_piramide[0], vertices_piramide[3]],
            [vertices_piramide[0], vertices_piramide[1], vertices_piramide[2]]
        ]
        piramide = Poly3DCollection(caras, facecolors="#FF9800", linewidths=1, edgecolors="black", alpha=0.8)
        ax.add_collection3d(piramide)
        ax.text(10, 0, altura3d + 1, "Triángulo", color="black", ha="center")

        # Configurar vista
        ax.set_xlim(-5, 15)
        ax.set_ylim(-5, 5)
        ax.set_zlim(0, 15)
        ax.set_box_aspect([1, 1, 1])
        ax.axis("off")

        # Mostrar dentro del Tkinter
        for widget in frame_canvas.winfo_children():
            widget.destroy()
        canvas_plt = FigureCanvasTkAgg(fig, master=frame_canvas)
        canvas_plt.draw()
        canvas_plt.get_tk_widget().pack()

    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

# ---------------- INTERFAZ ----------------
ventana = tk.Tk()
ventana.title("Figuras Geométricas 3D")
ventana.geometry("700x700")
ventana.configure(bg="#d0f0f5")

tk.Label(ventana, text="ÁREAS DE FIGURAS GEOMÉTRICAS 3D", font=("Arial", 16, "bold"), bg="#d0f0f5").pack(pady=10)

frame_inputs = tk.Frame(ventana, bg="#d0f0f5")
frame_inputs.pack(pady=5)

# Entradas
tk.Label(frame_inputs, text="Lado del Cuadrado:", bg="#d0f0f5").grid(row=0, column=0, sticky="e", padx=5, pady=3)
entry_lado = tk.Entry(frame_inputs)
entry_lado.grid(row=0, column=1)

tk.Label(frame_inputs, text="Radio del Círculo:", bg="#d0f0f5").grid(row=1, column=0, sticky="e", padx=5, pady=3)
entry_radio = tk.Entry(frame_inputs)
entry_radio.grid(row=1, column=1)

tk.Label(frame_inputs, text="Base del Triángulo:", bg="#d0f0f5").grid(row=2, column=0, sticky="e", padx=5, pady=3)
entry_base = tk.Entry(frame_inputs)
entry_base.grid(row=2, column=1)

tk.Label(frame_inputs, text="Altura del Triángulo:", bg="#d0f0f5").grid(row=3, column=0, sticky="e", padx=5, pady=3)
entry_altura = tk.Entry(frame_inputs)
entry_altura.grid(row=3, column=1)

# Botón calcular
tk.Button(ventana, text="Calcular y Mostrar en 3D", command=calcular_y_dibujar_3d,
          bg="#2196F3", fg="white", font=("Arial", 11, "bold")).pack(pady=10)

# Frame resultados
frame_resultados = tk.Frame(ventana, bg="#d0f0f5")
frame_resultados.pack(pady=5)

# Frame para el gráfico 3D
frame_canvas = tk.Frame(ventana, bg="#d0f0f5")
frame_canvas.pack(pady=10)

ventana.mainloop()
