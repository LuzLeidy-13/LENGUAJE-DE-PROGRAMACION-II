from datetime import datetime

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
            raise ValueError("La cantidad debe ser positiva")

    def salida_stock(self, cantidad):
        if cantidad > 0 and cantidad <= self.stock:
            self.stock -= cantidad
        else:
            raise ValueError("Stock insuficiente o cantidad inválida")

    def __str__(self):
        return f"{self.codigo} | {self.nombre} | S/ {self.precio:.2f} | Stock: {self.stock}"


class Inventario:
    def __init__(self):
        self.productos = {}
        self.movimientos = []

    def registrar_producto(self, producto):
        if producto.codigo not in self.productos:
            self.productos[producto.codigo] = producto
        else:
            raise ValueError("El producto ya existe")

    def entrada(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo].entrada_stock(cantidad)
            self.movimientos.append((datetime.now(), codigo, cantidad, "ENTRADA"))
        else:
            raise ValueError("Producto no encontrado")

    def salida(self, codigo, cantidad):
        if codigo in self.productos:
            self.productos[codigo].salida_stock(cantidad)
            self.movimientos.append((datetime.now(), codigo, cantidad, "SALIDA"))
        else:
            raise ValueError("Producto no encontrado")

    def mostrar_inventario(self):
        print("\n--- INVENTARIO ACTUAL ---")
        for producto in self.productos.values():
            print(producto)

    def reporte_movimientos(self):
        print("\n--- REPORTE DE MOVIMIENTOS ---")
        for fecha, codigo, cantidad, tipo in self.movimientos:
            print(f"{fecha.strftime('%d/%m/%Y %H:%M')} | {codigo} | {tipo} | {cantidad}")

    def reporte_valorizado(self):
        print("\n--- REPORTE VALORIZADO ---")
        total = 0
        for producto in self.productos.values():
            valor = producto.precio * producto.stock
            total += valor
            print(f"{producto.nombre}: S/ {valor:.2f}")
        print(f"TOTAL INVENTARIO: S/ {total:.2f}")


class SistemaInventario:
    """Interfaz del sistema"""
    def __init__(self):
        self.inventario = Inventario()

    def menu(self):
        while True:
            print("""
--- SISTEMA DE CONTROL DE INVENTARIOS ---
1. Registrar producto
2. Entrada de stock
3. Salida de stock
4. Mostrar inventario
5. Reporte de movimientos
6. Reporte valorizado
7. Salir
""")
            opcion = input("Seleccione una opción: ")

            try:
                if opcion == "1":
                    self.registrar_producto()
                elif opcion == "2":
                    self.entrada_stock()
                elif opcion == "3":
                    self.salida_stock()
                elif opcion == "4":
                    self.inventario.mostrar_inventario()
                elif opcion == "5":
                    self.inventario.reporte_movimientos()
                elif opcion == "6":
                    self.inventario.reporte_valorizado()
                elif opcion == "7":
                    print("Saliendo del sistema...")
                    break
                else:
                    print("Opción inválida")
            except ValueError as e:
                print("Error:", e)

    def registrar_producto(self):
        codigo = input("Código
