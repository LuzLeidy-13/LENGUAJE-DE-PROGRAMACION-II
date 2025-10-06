
import tkinter as tk
import gc

class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"Producto registrado: {self.nombre} - ${self.precio} en stock {self.cantidad}")

    def mostrar_informacion(self):
        return f"{self.nombre} - ${self.precio} en stock {self.cantidad}"

    def __del__(self):
        print(f"Producto eliminado: {self.nombre}")


inventario = []


def agregar_producto():
    nombre = entry_nombre.get()
    precio = entry_precio.get()
    cantidad = entry_cantidad.get()

    if nombre and precio.replace(".", "", 1).isdigit() and cantidad.isdigit():
        producto = Producto(nombre, float(precio), int(cantidad))
        inventario.append(producto)
        lista.insert(tk.END, producto.mostrar_informacion())
        # limpiar entradas
        entry_nombre.delete(0, tk.END)
        entry_precio.delete(0, tk.END)
        entry_cantidad.delete(0, tk.END)


def eliminar_productos():
    inventario.clear()
    gc.collect()
    lista.delete(0, tk.END)
    lista.insert(tk.END, "Productos eliminados")


# Ventana principal
ventana = tk.Tk()
ventana.title("Inventario de Productos")
ventana.configure(bg="lightcyan")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:", bg="lightcyan", fg="darkblue").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Precio:", bg="lightcyan", fg="darkblue").grid(row=1, column=0, padx=5, pady=5)
entry_precio = tk.Entry(ventana)
entry_precio.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Cantidad:", bg="lightcyan", fg="darkblue").grid(row=2, column=0, padx=5, pady=5)
entry_cantidad = tk.Entry(ventana)
entry_cantidad.grid(row=2, column=1, padx=5, pady=5)

# Botones
btn_agregar = tk.Button(ventana, text="Agregar Producto", command=agregar_producto,
                        bg="green", fg="white", activebackground="darkgreen")
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

btn_eliminar = tk.Button(ventana, text="Eliminar Productos", command=eliminar_productos,
                         bg="red", fg="white", activebackground="darkred")
btn_eliminar.grid(row=4, column=0, columnspan=2, pady=5)

# Listbox para mostrar el inventario
lista = tk.Listbox(ventana, width=50, height=10, bg="white", fg="black",
                   selectbackground="lightblue", selectforeground="black")
lista.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

ventana.mainloop()
print("fin de programa")

