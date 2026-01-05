# ==========================================
# SISTEMA DE CONTROL DE INVENTARIOS CON TKINTER
# Programación Orientada a Objetos + Encapsulamiento
# ==========================================

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


# -----------------------------
# CLASE PRODUCTO
# -----------------------------
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    # Getters
    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_stock(self):
        return self.__stock

    # Métodos de negocio
    def agregar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.__stock += cantidad

    def retirar_stock(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        if cantidad > self.__stock:
            raise ValueError("Stock insuficiente")
        self.__stock -= cantidad


# -----------------------------
# CLASE MOVIMIENTO
# -----------------------------
class Movimiento:
    def __init__(self, codigo, tipo, cantidad):
        self.codigo = codigo
        self.tipo = tipo
        self.cantidad = cantidad
        self.fecha = datetime.now()

    def __str__(self):
        return f"{self.fecha.strftime('%d/%m/%Y %H:%M:%S')} | {self.tipo} | {self.codigo} | {self.cantidad}"


# -----------------------------
# CLASE INVENTARIO
# -----------------------------
class Inventario:
    def __init__(self):
        self.__productos = {}
        self.__movimientos = []

    def registrar_producto(self, codigo, nombre, precio, stock):
        if codigo in self.__productos:
            raise ValueError("El producto ya existe")
        self.__productos[codigo] = Producto(codigo, nombre, precio, stock)

    def entrada_stock(self, codigo, cantidad):
        producto = self.__buscar_producto(codigo)
        producto.agregar_stock(cantidad)
        self.__movimientos.append(Movimiento(codigo, "ENTRADA", cantidad))

    def salida_stock(self, codigo, cantidad):
        producto = self.__buscar_producto(codigo)
        producto.retirar_stock(cantidad)
        self.__movimientos.append(Movimiento(codigo, "SALIDA", cantidad))

    def obtener_productos(self):
        return self.__productos.values()

    def obtener_movimientos(self):
        return self.__movimientos

    def __buscar_producto(self, codigo):
        if codigo not in self.__productos:
            raise ValueError("Producto no encontrado")
        return self.__productos[codigo]


# -----------------------------
# INTERFAZ GRÁFICA (TKINTER)
# -----------------------------
class AppInventario:
    def __init__(self, root):
        self.inventario = Inventario()
        self.root = root
        self.root.title("Sistema de Inventario")
        self.root.geometry("750x500")

        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill="both")

        self._crear_pestana_producto()
        self._crear_pestana_movimientos()
        self._crear_pestana_reportes()

    # -------- REGISTRAR PRODUCTOS --------
    def _crear_pestana_producto(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Productos")

        ttk.Label(frame, text="Código").grid(row=0, column=0)
        ttk.Label(frame, text="Nombre").grid(row=1, column=0)
        ttk.Label(frame, text="Precio").grid(row=2, column=0)
        ttk.Label(frame, text="Stock Inicial").grid(row=3, column=0)

        self.codigo_entry = ttk.Entry(frame)
        self.nombre_entry = ttk.Entry(frame)
        self.precio_entry = ttk.Entry(frame)
        self.stock_entry = ttk.Entry(frame)

        self.codigo_entry.grid(row=0, column=1)
        self.nombre_entry.grid(row=1, column=1)
        self.precio_entry.grid(row=2, column=1)
        self.stock_entry.grid(row=3, column=1)

        ttk.Button(frame, text="Registrar Producto", command=self.registrar_producto).grid(row=4, column=0, columnspan=2, pady=10)

        self.tabla = ttk.Treeview(frame, columns=("Codigo", "Nombre", "Precio", "Stock"), show="headings")
        for col in self.tabla["columns"]:
            self.tabla.heading(col, text=col)
        self.tabla.grid(row=5, column=0, columnspan=2, sticky="nsew")

    def registrar_producto(self):
        try:
            self.inventario.registrar_producto(
                self.codigo_entry.get(),
                self.nombre_entry.get(),
                float(self.precio_entry.get()),
                int(self.stock_entry.get())
            )
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Producto registrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -------- MOVIMIENTOS --------
    def _crear_pestana_movimientos(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Movimientos")

        ttk.Label(frame, text="Código").grid(row=0, column=0)
        ttk.Label(frame, text="Cantidad").grid(row=1, column=0)

        self.codigo_mov = ttk.Entry(frame)
        self.cantidad_mov = ttk.Entry(frame)
        self.codigo_mov.grid(row=0, column=1)
        self.cantidad_mov.grid(row=1, column=1)

        ttk.Button(frame, text="Entrada", command=self.entrada).grid(row=2, column=0)
        ttk.Button(frame, text="Salida", command=self.salida).grid(row=2, column=1)

    def entrada(self):
        try:
            self.inventario.entrada_stock(self.codigo_mov.get(), int(self.cantidad_mov.get()))
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Entrada registrada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def salida(self):
        try:
            self.inventario.salida_stock(self.codigo_mov.get(), int(self.cantidad_mov.get()))
            self.actualizar_tabla()
            messagebox.showinfo("Éxito", "Salida registrada")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # -------- REPORTES --------
    def _crear_pestana_reportes(self):
        frame = ttk.Frame(self.notebook)
        self.notebook.add(frame, text="Reportes")

        self.texto = tk.Text(frame, height=20)
        self.texto.pack(fill="both", expand=True)

        ttk.Button(frame, text="Ver Movimientos", command=self.ver_movimientos).pack(pady=5)

    def ver_movimientos(self):
        self.texto.delete(1.0, tk.END)
        for mov in self.inventario.obtener_movimientos():
            self.texto.insert(tk.END, str(mov) + "\n")

    # -------- ACTUALIZAR TABLA --------
    def actualizar_tabla(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        for p in self.inventario.obtener_productos():
            self.tabla.insert("", tk.END, values=(p.get_codigo(), p.get_nombre(), p.get_precio(), p.get_stock()))


# -----------------------------
# EJECUCIÓN
# -----------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = AppInventario(root)
    root.mainloop()
