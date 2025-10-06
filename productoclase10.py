import gc
class Producto:
    def __init__(self, nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        print(f"\n producto registrado {self.nombre} -$ {self.precio} en stook {self.cantidad}")

    def mostrar_informacion(self):
        print(f"{self.nombre} precio$ {self.precio} en stook {self.cantidad}")

    def __del__(self):
        print(f"producto eliminado {self.nombre}")



producto_datos = [("manzana",0.5, 1001),
                     ("pan",3.50,30)]

inventario = []
n = int(input("¿Cuántos productos quieres registrar?: "))

for i in range(n):
    nombre = input("Nombre del producto: ")
    precio = float(input("Precio: "))
    cantidad = int(input("Cantidad en stock: "))
    producto_datos.append((nombre, precio, cantidad))

inventario.clear()
del producto
gc.collect()
print("fin de programa")
