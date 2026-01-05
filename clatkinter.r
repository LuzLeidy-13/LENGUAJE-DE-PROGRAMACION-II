import tkinter as tk

# -----------------------
#  Lógica de cálculo
# -----------------------
def presionar(valor):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + valor)

def limpiar():
    entrada.delete(0, tk.END)

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

# -----------------------
#  Ventana principal
# -----------------------
ventana = tk.Tk()
ventana.title("Calculadora Infantil")
ventana.geometry("350x500")
ventana.resizable(False, False)
ventana.config(bg="#6a5acd")  # morado bonito

# Caja de resultados
entrada = tk.Entry(ventana, font=("Arial", 28), bd=5, relief="ridge", justify="right")
entrada.pack(fill="both", padx=10, pady=15)

# -----------------------
#  Botones estilo celular
# -----------------------

estilo = {
    "font": ("Comic Sans MS", 20, "bold"),
    "width": 4,
    "height": 2,
    "bd": 4,
    "relief": "raised"
}

# Frame general de botones
frame = tk.Frame(ventana, bg="#6a5acd")
frame.pack()

# Colores infantiles
color_num = "#ffcc00"      # amarillo
color_ops = "#ff6699"      # rosado
color_c = "#66ccff"        # celeste
color_equal = "#77dd77"    # verde

# Crea un botón con color
def boton(parent, texto, color, comando):
    return tk.Button(
        parent, text=texto, bg=color, command=comando,
        activebackground=color, **estilo
    )

# -----------------------
# Distribución tipo celular
# -----------------------

# Fila 1
fila1 = tk.Frame(frame, bg="#6a5acd")
fila1.pack()
boton(fila1, "7", color_num, lambda: presionar("7")).pack(side="left", padx=5, pady=5)
boton(fila1, "8", color_num, lambda: presionar("8")).pack(side="left", padx=5, pady=5)
boton(fila1, "9", color_num, lambda: presionar("9")).pack(side="left", padx=5, pady=5)
boton(fila1, "+", color_ops, lambda: presionar("+")).pack(side="left", padx=5, pady=5)

# Fila 2
fila2 = tk.Frame(frame, bg="#6a5acd")
fila2.pack()
boton(fila2, "4", color_num, lambda: presionar("4")).pack(side="left", padx=5, pady=5)
boton(fila2, "5", color_num, lambda: presionar("5")).pack(side="left", padx=5, pady=5)
boton(fila2, "6", color_num, lambda: presionar("6")).pack(side="left", padx=5, pady=5)
boton(fila2, "-", color_ops, lambda: presionar("-")).pack(side="left", padx=5, pady=5)

# Fila 3
fila3 = tk.Frame(frame, bg="#6a5acd")
fila3.pack()
boton(fila3, "1", color_num, lambda: presionar("1")).pack(side="left", padx=5, pady=5)
boton(fila3, "2", color_num, lambda: presionar("2")).pack(side="left", padx=5, pady=5)
boton(fila3, "3", color_num, lambda: presionar("3")).pack(side="left", padx=5, pady=5)
boton(fila3, "×", color_ops, lambda: presionar("*")).pack(side="left", padx=5, pady=5)

# Fila 4
fila4 = tk.Frame(frame, bg="#6a5acd")
fila4.pack()
boton(fila4, "0", color_num, lambda: presionar("0")).pack(side="left", padx=5, pady=5)
boton(fila4, ".", color_num, lambda: presionar(".")).pack(side="left", padx=5, pady=5)
boton(fila4, "C", color_c, limpiar).pack(side="left", padx=5, pady=5)
boton(fila4, "÷", color_ops, lambda: presionar("/")).pack(side="left", padx=5, pady=5)

# Fila 5 (igual grande)
fila5 = tk.Frame(frame, bg="#6a5acd")
fila5.pack()
tk.Button(
    fila5, text="=", bg=color_equal, activebackground=color_equal,
    font=("Comic Sans MS", 23, "bold"), width=16, height=2,
    bd=5, relief="ridge", command=calcular
).pack(pady=10)

# Ejecutar
ventana.mainloop()
