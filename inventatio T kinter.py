from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

# =============================
# MODELO (POO)
# =============================
class Producto:
    def __init__(self, codigo, nombre, precio, stock=0):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def entrada_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad
        else:
            raise ValueError("Cantidad inválida")

    def salida_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError("Stock insuficiente")


class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def registrar_producto(self, p):
        if p.codigo in self.productos:
            raise ValueError("Producto ya existe")
        self.productos[p.codigo] = p

    def entrada(self, codigo, cantidad):
        self.productos[codigo].entrada_stock(cantidad)
        self.movimientos.append((datetime.now(), codigo, cantidad, "ENTRADA"))

    def salida(self, codigo, cantidad):
        self.productos[codigo].salida_stock(cantidad)
        self.movimientos.append((datetime.now(), codigo, cantidad, "SALIDA"))

    def exportar_excel(self):
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title = "Inventario"
        ws.append(["Código", "Nombre", "Precio", "Stock", "Valor"])
        for p in self.productos.values():
            ws.append([p.codigo, p.nombre, p.precio, p.stock, p.precio*p.stock])
        wb.save("inventario.xlsx")

    def generar_voucher_pdf(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        c = canvas.Canvas("voucher.pdf", pagesize=A4)
        y = 800
        c.setFont("Helvetica-Bold", 12)
        c.drawString(50, y, "VOUCHER DE INVENTARIO")
        y -= 40
        c.setFont("Helvetica", 10)
        for p in self.productos.values():
            c.drawString(50, y, f"{p.codigo} - {p.nombre} | Stock: {p.stock} | S/ {p.precio}")
            y -= 20
        c.save()

    def generar_codigos_barras(self):
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfgen import canvas
        from reportlab.graphics.barcode import code128
        from reportlab.lib.units import mm
        c = canvas.Canvas("codigos_barras.pdf", pagesize=A4)
        y = 750
        for p in self.productos.values():
            bc = code128.Code128(p.codigo, barHeight=20*mm)
            bc.drawOn(c, 50, y)
            c.drawString(50, y-15, p.nombre)
            y -= 80
        c.save()


# =============================
# LOGIN
# =============================
class Login:
    def __init__(self, root):
        self.root = root
        root.title("Login")
        root.geometry("300x200")
        root.resizable(False, False)

        tk.Label(root, text="Sistema de Inventarios", font=("Arial", 14, "bold")).pack(pady=10)

        tk.Label(root, text="Usuario").pack()
        self.user = tk.Entry(root)
        self.user.pack()

        tk.Label(root, text="Contraseña").pack()
        self.passw = tk.Entry(root, show="*")
        self.passw.pack()

        tk.Button(root, text="Ingresar", bg="#2ecc71", fg="white",
                  command=self.validar).pack(pady=10)

    def validar(self):
        if self.user.get() == "admin" and self.passw.get() == "1234":
            self.root.destroy()
            main_app()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")


# =============================
# INTERFAZ PRINCIPAL
# =============================
class InventarioGUI:
    def __init__(self, root):
        self.inv = Inventario()
        self.root = root
        root.title("Sistema de Control de Inventarios")
        root.geometry("900x500")

        ttk.Style().theme_use("clam")

        tk.Label(root, text="CONTROL DE INVENTARIOS",
                 font=("Arial", 16, "bold"), fg="#2c3e50").pack(pady=10)

        self.formulario()
        self.tabla()
        self.botones()

    def formulario(self):
        f = ttk.LabelFrame(self.root, text="Registro de Producto")
        f.pack(padx=10, pady=5, fill="x")

        ttk.Label(f, text="Código").grid(row=0, column=0)
        ttk.Label(f, text="Nombre").grid(row=0, column=2)
        ttk.Label(f, text="Precio").grid(row=1, column=0)
        ttk.Label(f, text="Stock").grid(row=1, column=2)

        self.e_codigo = ttk.Entry(f)
        self.e_nombre = ttk.Entry(f)
        self.e_precio = ttk.Entry(f)
        self.e_stock = ttk.Entry(f)

        self.e_codigo.grid(row=0, column=1)
        self.e_nombre.grid(row=0, column=3)
        self.e_precio.grid(row=1, column=1)
        self.e_stock.grid(row=1, column=3)

        ttk.Button(f, text="Registrar", command=self.registrar).grid(
            row=2, column=0, columnspan=4, pady=5)

    def tabla(self):
        cols = ("Código", "Nombre", "Precio", "Stock")
        self.tv = ttk.Treeview(self.root, columns=cols, show="headings", height=8)
        for c in cols:
            self.tv.heading(c, text=c)
            self.tv.column(c, anchor="center")
        self.tv.pack(expand=True, fill="both", padx=10, pady=5)

    def botones(self):
        b = ttk.Frame(self.root)
        b.pack(pady=5)

        ttk.Button(b, text="Entrada", command=lambda: self.mov(True)).grid(row=0, column=0, padx=3)
        ttk.Button(b, text="Salida", command=lambda: self.mov(False)).grid(row=0, column=1, padx=3)
        ttk.Button(b, text="Excel", command=self.excel).grid(row=0, column=2, padx=3)
        ttk.Button(b, text="Voucher PDF", command=self.voucher).grid(row=0, column=3, padx=3)
        ttk.Button(b, text="Códigos Barras", command=self.barras).grid(row=0, column=4, padx=3)

    def registrar(self):
        try:
            p = Producto(self.e_codigo.get(), self.e_nombre.get(),
                         float(self.e_precio.get()), int(self.e_stock.get()))
            self.inv.registrar_producto(p)
            self.refrescar()
            messagebox.showinfo("OK", "Producto registrado")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def mov(self, entrada=True):
        sel = self.tv.selection()
        if not sel:
            messagebox.showwarning("Atención", "Seleccione un producto")
            return
        codigo = self.tv.item(sel)['values'][0]
        cant = simpledialog.askinteger("Cantidad", "Ingrese cantidad")
        if cant is None:
            return
        try:
            if entrada:
                self.inv.entrada(codigo, cant)
            else:
                self.inv.salida(codigo, cant)
            self.refrescar()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refrescar(self):
        for i in self.tv.get_children():
            self.tv.delete(i)
        for p in self.inv.productos.values():
            self.tv.insert("", "end", values=(p.codigo, p.nombre, p.precio, p.stock))

    def excel(self):
        self.inv.exportar_excel()
        messagebox.showinfo("Excel", "inventario.xlsx generado")

    def voucher(self):
        self.inv.generar_voucher_pdf()
        messagebox.showinfo("PDF", "voucher.pdf generado")

    def barras(self):
        self.inv.generar_codigos_barras()
        messagebox.showinfo("PDF", "codigos_barras.pdf generado")


def main_app():
    root = tk.Tk()
    InventarioGUI(root)
    root.mainloop()


if __name__ == "__main__":
    login = tk.Tk()
    Login(login)
    login.mainloop()
